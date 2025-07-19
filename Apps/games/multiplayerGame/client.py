import socket
import pickle
import pygame

PORT = 7500
SERVER = "192.168.29.78"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
playing = True
delta_time = 0.1
clock = pygame.time.Clock()
playerData = [8, 8, 'NA', 'o']
pygame.init()
screen = pygame.display.set_mode((480, 480))

imgs = [pygame.image.load('grass.png').convert(),
              pygame.image.load('player.png').convert()]


def drawMap(gameMap, imgs):
    y = 0
    for row in gameMap:
        x = 0
        for item in row:
            if item == '#':
                screen.blit(imgs[0], (x, y))
            else:
                screen.blit(imgs[1], (x, y))
            x += 32
        y += 32

print("Connected to server.")
playerData[3] = input("what character should your player be? ")
try:
    while playing:
        playerData[2] = 'NA'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerData[1] -= 1
                    playerData[2] = 'w'
                elif event.key == pygame.K_a:
                    playerData[0] -= 1
                    playerData[2] = 'a'
                elif event.key == pygame.K_s:
                    playerData[1] += 1
                    playerData[2] = 's'
                elif event.key == pygame.K_d:
                    playerData[0] += 1
                    playerData[2] = 'd'
                else:
                    continue  # skip invalid keys
        print(playerData)
        serialized = pickle.dumps(playerData)
        client.sendall(serialized)

        gameMap = pickle.loads(client.recv(10000))

        screen.fill((0, 0, 0))
        drawMap(gameMap, imgs)
        pygame.display.flip()

        delta_time = clock.tick(60)
        delta_time = max(0.001, min(0.1, delta_time))

finally:
    client.close()
    pygame.quit()