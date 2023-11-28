import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)

server_socket.bind(server_address)

server_socket.listen(5)

print("Server is listening ...")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

data = client_socket.recv(1024)
print(f"Received data from client : {data.decode()}")

if b"block" in data:
    response = "Request blocked by firewall."
else:
    response = "Response from server: Hello, client!"

client_socket.sendall(response.encode())

client_socket.close()
server_socket.close()
