import socket
import pickle
import threading

PORT = 7500
SERVER = "192.168.29.94"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen(2)

def handle_players(client, addr):
    while True:

        try:
            print('Connected')

            data = b''
            while True:
                data = client.recv(4096)
                if not data:
                    break
                recv_object = pickle.loads(data)
                print(f'Recieved Object: {recv_object} from {addr}')

                # add the players to the map

                gameMap[recv_object[1]][recv_object[0]] = recv_object[3]

                if recv_object[2] == 'w':
                    gameMap[(recv_object[1] + 1)][recv_object[0]] = '#'
                elif recv_object[2] == 'a':
                    gameMap[recv_object[1]][(recv_object[0] + 1)] = '#'
                elif recv_object[2] == 's':
                    gameMap[(recv_object[1] - 1)][recv_object[0]] = '#'
                elif recv_object[2] == 'd':
                    gameMap[recv_object[1]][(recv_object[0] - 1)] = '#'

                serialized = pickle.dumps(gameMap)
                client.sendall(serialized)

        finally:
            print(f'{addr} disconnected')
            client.close()

gameMap = []

for i in range(0, 16):
    row = []
    for j in range(0, 16):
        row.append('#')
    gameMap.append(row)

print('Waiting for connections...')
client, addr = server.accept()
print(f'Player 2 connected from {addr}')

thread = threading.Thread(target=handle_players, args=(client, addr))
thread.start()
print('Waiting for second player')
client2, addr2 = server.accept()
print(f'Player 2 connected from {addr}')

thread2 = threading.Thread(target=handle_players, args=(client2, addr2))
thread2.start()