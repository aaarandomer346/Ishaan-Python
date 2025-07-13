import socket
import pickle

PORT = 7500
SERVER = "192.168.29.94"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen(1)

while True:
    print('Waiting for connection...')
    client, addr = server.accept()

    try:
        print('Connected')

        data = b''
        while True:
            data = client.recv(4096)
            if not data:
                break
            recv_object = pickle.loads(data)
            print(f'Recieved Object: {recv_object}')


    finally:
        client.close()