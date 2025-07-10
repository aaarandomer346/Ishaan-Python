# so basically a game where you can roam around infinitly and discover stuff
# Possible ideas:
    # a game where you go around in a space ship and find new planets to colinize and stuff
        # requires:
            # an infinite space map that generates:
                # planets
                # asteroids
                # cool stuff
            # a auto-created map for each planet

# TODO:
    # Make a small map generator as text                                            DONE
    # make a character that can move around                                         DONE
        # Make the map that moves instead of the player                             DONE
            # setup a big map that the player moves around in (1 chunk)             DONE
            # if the player reaches the end, stop them (for now)                    NA IM GOOD
    # Make the world actually infinite                                              DONE
        # Remove the code that stopped the player                                   NEVER ADDED IT
        # replace with code where:                                                  DONE
            # if the player tries to go somewhere that isnt generated:              DONE
                # generate a new row/column                                         DONE
            # to see if a new row/column has to be loaded:                          DONE
                # if the map moves into a place that hasnt been generated:          DONE
                    # generate the next chunk                                       DONE
    # Turn the map from text based into visual

# NOTE:
    # "Chunk" Refers to a block in the world, a grid of sorts
    # each chunk is 15x15, player can only see a 15x15 area

    # Each chunk has a set amount of stuff that can generate in it,
    # for example, 1 greenland chunk can only have 15 trees, 3 rocks, etc.
    # to spice it up it can be left up to random chance of how many of something there are
    # but, where it is placed is always random
    # but somethings have higher priority than others, for example:
        # something that is larger than 1 tile
        # stuff that i want more common than other stuff

    # make the game cool



import random as random
import pygame

def giveVisualMap(fullMap, playerX, playerY):
    visualMap = []
    for i in range(len(fullMap)):
        row = []
        for j in range(len(fullMap[playerY])):
            if i >= playerY - 7 and j >= playerX - 7 and i <= playerY + 7 and j <= playerX + 7:
                row.append(fullMap[i][j])
        if len(row) != 0:
            visualMap.append(row)
    return visualMap

def drawPlayer(fullMap, playerX, playerY, direction):
    if direction != 'invalid':
        if direction == 'up':
            fullMap[playerY+1][playerX] = '#'
        elif direction == 'left':
            fullMap[playerY][playerX+1] = '#'
        elif direction == 'down':
            fullMap[playerY-1][playerX] = '#'
        elif direction == 'right':
            fullMap[playerY][playerX-1] = '#'
    fullMap[playerY][playerX] = 'o'
    return fullMap

def movePlayer(direction, playerX, playerY, fullMap):
    if direction == 'up':
        playerY -= 1
        drawPlayer(fullMap, playerX, playerY, direction)
        return playerX, playerY, direction
    elif direction == 'left':
        playerX -= 1
        drawPlayer(fullMap, playerX, playerY, direction)
        return playerX, playerY, direction
    elif direction == 'down':
        playerY += 1
        drawPlayer(fullMap, playerX, playerY, direction)
        return playerX, playerY, direction
    elif direction == 'right':
        playerX += 1
        drawPlayer(fullMap, playerX, playerY, direction)
        return playerX, playerY, direction
    else:
        return playerX, playerY, "-"

def extendMap(fullMap, direction, playerX, playerY):
    # 7 for top and left
    # 25 for bottom and right

    # just extend by 1 tile
    if direction == 'up':
        # top
        for j in range(0, 15):
            newRow = []
            for i in range(0, len(fullMap[playerY])):
                treeChance = random.randint(1, 10)
                if treeChance == 1:
                    newRow.append('T')
                else:
                    newRow.append('#')
            fullMap.insert(0, newRow)
            playerY += 1
    elif direction == 'left':
        # left
        for i in range(0, 15):
            for i in fullMap:
                treeChance = random.randint(1, 10)
                if treeChance == 1:
                    i.insert(0, 'T')
                else:
                   i.insert(0, '#')
            playerX += 1
    elif direction == 'down':
        # down
        for j in range(0, 15):
            newRow = []
            for i in range(0, len(fullMap[playerY])):
                treeChance = random.randint(1, 10)
                if treeChance == 1:
                    newRow.append('T')
                else:
                    newRow.append('#')
            fullMap.append(newRow)
    elif direction == 'right':
        # right
        for j in range(0, 15):
            for i in fullMap:
                treeChance = random.randint(1, 10)
                if treeChance == 1:
                    i.append('T')
                else:
                    i.append('#')
    return fullMap, playerX, playerY

def drawMap(visualMap, imgs):
    y = 0
    for row in visualMap:
        x = 0
        for item in row:
            if item == '#':
                screen.blit(imgs[0], (x, y))
            elif item == "T":
                screen.blit(imgs[1], (x, y))
            elif item == "o":
                screen.blit(imgs[2], (x, y))
            x += 32
        y += 32

mapHeight = 15
mapLength = 15
playerX = 8 # add 1 for true location
playerY = 8 # add 1 for true location
fullMap = []

pygame.init()
delta_time = 0.1
clock = pygame.time.Clock()

screen = pygame.display.set_mode((480, 480))

imgs = [pygame.image.load('Apps\games\infiniGame\grass.png').convert(),
              pygame.image.load('Apps\games\infiniGame\\tree.png').convert(),
              pygame.image.load('Apps\games\infiniGame\player.png').convert()]

for i in range(mapHeight):
    mapcolumn = []
    for j in range(mapLength):
            mapcolumn.append("#")
    fullMap.append(mapcolumn)
numOfTrees = random.randint(5, 30)
treesAdded = 0
while treesAdded <= numOfTrees:
    row = random.randint(0, mapHeight-1)
    column = random.randint(0, mapLength-1)
    if (fullMap[row][column] != "#"):
        continue
    fullMap[row][column] = "T"
    treesAdded+=1
drawPlayer(fullMap, playerX, playerY, 'invalid')

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerX, playerY, direction = movePlayer('up', playerX, playerY, fullMap)
            elif event.key == pygame.K_DOWN:
                playerX, playerY, direction = movePlayer('down', playerX, playerY, fullMap)
            elif event.key == pygame.K_LEFT:
                playerX, playerY, direction = movePlayer('left', playerX, playerY, fullMap)
            elif event.key == pygame.K_RIGHT:
                playerX, playerY, direction = movePlayer('right', playerX, playerY, fullMap)
    if playerX < 7 or playerY < 7 or playerX > len(fullMap[playerY]) - 7 or playerY > len(fullMap) - 7:
        fullMap, playerX, playerY = extendMap(fullMap, direction, playerX, playerY)

    drawMap(giveVisualMap(fullMap, playerX, playerY), imgs)
    pygame.display.flip()

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()