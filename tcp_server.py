# tcp_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("🖥 TCP Server is waiting for connection...")
conn, addr = server.accept()
print("✅ Connected by", addr)

data = conn.recv(1024).decode()
print("📥 Received from client:", data)

conn.send("Hello from server!".encode())
conn.close()