import socket
import ssl
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 10111))
server_socket.listen(1)

print("server is listening on 10111")

ssl_context =ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    certfile=r"server.crt",
    keyfile=r"server.key"
    )

print("server is listening on port 10111 with secure connection")

conn, addr = server_socket.accept()

secure_socket = ssl_context.wrap_socket(conn, server_side=True)

print(f"Connection from {addr}")

data = secure_socket.recv(1024)
print(f"Received from client: {data.decode()}")

with open("received_file.txt","wb") as f:
    print("Ready to receive file")
    while True:
        f.write(data)
        data = secure_socket.recv(1024)
        
        if not data:
            break
        
print("File received successfully")

secure_socket.close()
