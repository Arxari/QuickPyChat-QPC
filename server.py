import socket, threading

host, port = '0.0.0.0', 55555
clients = []

def broadcast(message, sender):
    [client.send((sender + ": " + message).encode('utf-8')) for client in clients if client != sender]

def handle_client(client, addr):
    username = client.recv(1024).decode('utf-8')
    clients.append(client)
    print(f"{username} connected from {addr}")

    threading.Thread(target=lambda: receive_messages(client, username)).start()
    threading.Thread(target=lambda: send_messages(client)).start()

def receive_messages(client, username):
    while True:
        try: print(client.recv(1024).decode('utf-8'))
        except: clients.remove(client); break

def send_messages(client):
    while True: client.send(input().encode('utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Server listening on {host}:{port}")

    while True: handle_client(*server.accept())

if __name__ == "__main__": start_server()