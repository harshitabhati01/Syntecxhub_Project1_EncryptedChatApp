import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST = "127.0.0.1"
PORT = 12345

KEY = b"1234567890123456"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print("Server Started...")
print("Waiting for connections...")

def handle_client(client):
    while True:
        try:
            data = client.recv(1024)

            if not data:
                break

            iv = data[:16]
            encrypted_message = data[16:]

            cipher = AES.new(KEY, AES.MODE_CBC, iv)

            decrypted_message = cipher.decrypt(encrypted_message)

            message = unpad(
                decrypted_message,
                AES.block_size
            ).decode()

            print("Client:", message)

            with open("chatlog.txt", "a") as file:
                file.write("Client: " + message + "\n")

        except Exception as e:
            print("ERROR:", e)
            break

    client.close()

while True:
    client, address = server.accept()

    print("Connected:", address)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()