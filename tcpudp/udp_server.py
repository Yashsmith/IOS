# udp_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))

print("🖥 UDP Server is waiting for message...")
data, addr = server.recvfrom(1024)
print("📥 Received from client:", data.decode())

server.sendto("Hello from server!".encode(), addr)