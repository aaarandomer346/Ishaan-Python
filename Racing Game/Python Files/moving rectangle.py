import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

running = True

clock = pygame.time.Clock()
# (top-left), (top-right), (bottom-right), (bottum-left)
points = [(450, 450), (550, 450), (550, 600), (450, 600)]
print(points[0][0])
degreeCCW = -1 # counter clockwise
degreeCW = 1 # clockwise
degreeRotated = 270

turningCW = False
turningCCW = False

movingForward = False

def rotate(angle, points):
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)

    rotated = []
    for x, y in points:
        x -= cx
        y -= cy

        rad = math.radians(angle)
        xr = x * math.cos(rad) - y * math.sin(rad)
        yr = x * math.sin(rad) + y * math.cos(rad)

        xr += cx
        yr += cy

        rotated.append((xr, yr))


    return rotated

def move(points, speed, angle):
    moved = []

    rad = math.radians(angle)
    dx = math.cos(rad) * speed
    dy = math.sin(rad) * speed

    for x, y in points:
        x += dx
        y += dy

        moved.append((x, y))

    return moved

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get(): # for each event in a pygame event
        if event.type == pygame.QUIT: # if the pygame event is closing the winodw
            running = False # stop the while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                turningCW = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                turningCW = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                turningCCW = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                turningCCW = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movingForward = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movingForward = False


    if turningCW:
        points = rotate(degreeCW, points)
        if degreeRotated >= 360:
            degreeRotated = 0
        degreeRotated += 1
    elif turningCCW:
        points = rotate(degreeCCW, points)
        if degreeRotated < 0:
            degreeRotated = 360
        degreeRotated -= 1
    
    if movingForward:
        points = move(points, 5, degreeRotated)

    
    pygame.draw.polygon(screen, (255, 255, 255), points)

    pygame.display.flip() 

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))
    print(points)
    print(degreeRotated)
    

pygame.quit() 