import socket, threading

server_host, server_port = 'SERVER_PUBLIC_IP_OR_DOMAIN', 55555

def receive_messages(client):
    while True: print(client.recv(1024).decode('utf-8'))

def send_messages(client):
    while True: client.send(input().encode('utf-8'))

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: client.connect((server_host, server_port))
    except: print("You (probaly) did something wrong bruh"); return

    threading.Thread(target=lambda: receive_messages(client)).start()
    threading.Thread(target=lambda: send_messages(client)).start()

    client.send(input("What do you want people to call you?: ").encode('utf-8'))

if __name__ == "__main__": connect_to_server()
