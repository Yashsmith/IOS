# udp_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("Hello from client!".encode(), ('localhost', 12345))

data, addr = client.recvfrom(1024)
print("📥 Received from server:", data.decode())