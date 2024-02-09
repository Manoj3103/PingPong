import socket
import pickle
import threading

# Define constants
HOST = '127.0.0.1'
PORT = 5555

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Store client sockets and their corresponding paddles
clients = []
paddles = []

def handle_client(client, idx):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            paddles[idx] = pickle.loads(data)
        except Exception as e:
            print(e)
            break

    client.close()

def start_server():
    global clients, paddles

    print("Server is listening...")
    
    while True:
        client, address = server_socket.accept()
        print(f"Connection from {address} has been established!")

        clients.append(client)
        paddles.append(None)

        thread = threading.Thread(target=handle_client, args=(client, len(clients) - 1))
        thread.start()

if __name__ == "__main__":
    start_server()
