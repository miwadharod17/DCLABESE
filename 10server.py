import socket
import threading

def handle_client(conn, addr):
    print(f"[THREAD {threading.get_ident()}] Handling client {addr}")
    
    msg = conn.recv(1024).decode()
    print(f"[THREAD {threading.get_ident()}] Received: {msg}")
    
    conn.send(b"Message processed")
    conn.close()

# ---------------- SERVER ----------------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(5)

print("Multithreaded Server Running...\n")

while True:
    conn, addr = server.accept()
    print(f"New connection from {addr}")

    # CREATE NEW THREAD for every client
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()
