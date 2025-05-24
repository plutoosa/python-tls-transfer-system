import socket
import ssl

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(r"server.crt") #incorrect server certificate 

secure_socket =  context.wrap_socket(client_socket, server_hostname="localhost")

secure_socket.connect(("localhost", 10111))
secure_socket.sendall(b"Hello, secure server!")

#allows client to send files
with open("file_to_send.txt", "rb") as file:
    file_data = file.read()
    secure_socket.sendall(file_data)
    
print("File successfully sent")
secure_socket.close()