import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 55555        # Port to listen on

# List to store all client connections
clients = []

# Function to handle each client's connection
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            # Broadcast the message to all other clients
            broadcast(message, client_socket)
        
        except Exception as e:
            print(f"Connection closed by {client_address}")
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast a message to all clients except the sender
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                # If there's an issue sending message to a client, remove it from the list
                print(f"Connection closed by {client.getpeername()}")
                clients.remove(client)
                client.close()

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Accept incoming connections and handle each in a new thread
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
