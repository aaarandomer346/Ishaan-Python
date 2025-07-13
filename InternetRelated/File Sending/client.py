import socket
import pickle
import pygame

PORT = 7500
SERVER = "192.168.29.94"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
playing = True
delta_time = 0.1
clock = pygame.time.Clock()
pos = [0, 0]
try:
    while playing == True:
        direction = input("Where do you want to move? ")
        if direction == 'w':
            pos[1] += 1
        elif direction == 'a':
            pos[0] -= 1
        elif direction == 's':
            pos[1] -= 1
        elif direction == 'd':
            pos[0] += 1
        elif direction == 'quit':
            playing = False
        print(pos)
        serialized = pickle.dumps(pos)
        client.sendall(serialized)

        delta_time = clock.tick(60)
        delta_time = max(0.001, min(0.1, delta_time))
finally:
    client.close()