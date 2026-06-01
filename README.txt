Project Name: Encrypted Chat Application

Objective:
To develop a secure client-server chat application using Python.

Project Description:
- Built a client-server chat application using TCP sockets.
- Implemented AES-CBC encryption for secure communication.
- Used a pre-shared secret key for encryption and decryption.
- Implemented safe IV (Initialization Vector) handling.
- Supported multiple clients using multithreading.
- Logged received messages into chatlog.txt.

Features:
- TCP Socket Communication
- AES-CBC Encryption
- Secure IV Usage
- Pre-Shared Key Handling
- Multiple Client Support
- Message Logging

Technologies Used:
- Python
- Socket Programming
- Multithreading
- PyCryptodome
- AES Encryption (CBC Mode)

Files Included:
- server.py
- client.py
- chatlog.txt
- README.txt

How To Run:

1. Install library:
   pip install pycryptodome

2. Run server:
   python server.py

3. Open a new terminal and run client:
   python client.py

4. Send messages from the client terminal.

Security Implementation:
- AES Encryption
- CBC Mode
- Random IV Generation
- Pre-Shared Secret Key

Outcome:
Successfully developed a secure encrypted chat application that supports multiple clients, secure message transmission, and message logging.