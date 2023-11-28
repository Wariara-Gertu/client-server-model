import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)

client_socket.connect(server_address)

request = "Sending request to the server"
client_socket.sendall(request.encode())

response = client_socket.recv(1024)
print(f"Received from server: {response.decode()}")

client_socket.close()
