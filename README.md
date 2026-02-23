# Command & Control (C2) Reverse Shell

## 🚩 Overview
A lightweight Python-based Remote Access Trojan (RAT) designed to bypass traditional firewall restrictions by establishing an outbound TCP connection from the target machine back to the attacker's listening server. 

## ⚙️ Technical Mechanisms
* **Reverse TCP Connection:** The client initiates the connection to circumvent inbound NAT and firewall rules.
* **Remote Code Execution:** Utilizes Python's `subprocess` module to execute system-level shell commands dynamically.
* **Continuous Listening:** The server implements a continuous binding loop via `socket.SO_REUSEADDR` for stable session management.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** `socket`, `subprocess`, `os`
* **Protocols:** TCP/IP
