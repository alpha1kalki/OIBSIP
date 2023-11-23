import socket
import threading

# Client configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 55555        # Server's port number

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print("Connection closed by server")
            break

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Start a thread to handle receiving messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Start sending messages
while True:
    message = input()
    client.send(message.encode('utf-8'))

# Close the client socket
client.close()
