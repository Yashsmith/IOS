# tcp_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

client.send("Hello from client!".encode())
data = client.recv(1024).decode()
print("📥 Received from server:", data)

client.close()