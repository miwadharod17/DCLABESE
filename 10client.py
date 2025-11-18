import socket

client = socket.socket()
client.connect(("localhost", 5000))

msg = input("Enter message: ")
client.send(msg.encode())

response = client.recv(1024).decode()
print("Server replied:", response)

client.close()
