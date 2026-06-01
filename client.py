import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

HOST = "127.0.0.1"
PORT = 12345

KEY = b"1234567890123456"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to Server")

while True:

    message = input("You: ")

    iv = get_random_bytes(16)

    cipher = AES.new(
        KEY,
        AES.MODE_CBC,
        iv
    )

    encrypted_message = cipher.encrypt(
        pad(
            message.encode(),
            AES.block_size
        )
    )

    client.sendall(
        iv + encrypted_message
    )