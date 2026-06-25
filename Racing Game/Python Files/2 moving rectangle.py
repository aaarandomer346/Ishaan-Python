import pygame
import math

pygame.init()

screen = pygame.display.set_mode((2500, 1500))

running = True

clock = pygame.time.Clock()
# (top-left), (top-right), (bottom-right), (bottum-left)
pointsCarOne = [(450, 450), (550, 450), (550, 600), (450, 600)]
pointsCarTwo = [(450, 450), (550, 450), (550, 600), (450, 600)]
degreeCCW = -5 # counter clockwise
degreeCW = 5 # clockwise
degreeRotatedCarOne = 270
degreeRotatedCarTwo = 270

turningCWCarOne = False
turningCCWCarOne = False

turningCWCarTwo = False
turningCCWCarTwo = False

movingForwardCarOne = False
movingForwardCarTwo = False

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
                turningCWCarOne = True
            if event.key == pygame.K_a:
                turningCCWCarOne = True
            if event.key == pygame.K_w:
                movingForwardCarOne = True

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                turningCWCarOne = False
            if event.key == pygame.K_a:
                turningCCWCarOne = False
            if event.key == pygame.K_w:
                movingForwardCarOne = False

            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                turningCWCarTwo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                turningCWCarTwo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turningCCWCarTwo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                turningCCWCarTwo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movingForwardCarTwo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                movingForwardCarTwo = False


    if turningCWCarOne:
        pointsCarOne = rotate(degreeCW, pointsCarOne)
        degreeRotatedCarOne += degreeCW
        if degreeRotatedCarOne >= 360:
            degreeRotatedCarOne = 0
    elif turningCCWCarOne:
        pointsCarOne = rotate(degreeCCW, pointsCarOne)
        degreeRotatedCarOne += degreeCCW
        if degreeRotatedCarOne < 0:
            degreeRotatedCarOne = 355
    
    if movingForwardCarOne:
        pointsCarOne = move(pointsCarOne, 15, degreeRotatedCarOne)

    
    if turningCWCarTwo:
        pointsCarTwo = rotate(degreeCW, pointsCarTwo)
        degreeRotatedCarTwo += degreeCW
        if degreeRotatedCarTwo >= 360:
            degreeRotatedCarTwo = 0
    elif turningCCWCarTwo:
        pointsCarTwo = rotate(degreeCCW, pointsCarTwo)
        degreeRotatedCarTwo += degreeCCW
        if degreeRotatedCarTwo < 0:
            degreeRotatedCarTwo = 355
    
    if movingForwardCarTwo:
        pointsCarTwo = move(pointsCarTwo, 15, degreeRotatedCarTwo)

    
    pygame.draw.polygon(screen, (0, 0, 255), pointsCarOne)
    pygame.draw.polygon(screen, (255, 0, 0), pointsCarTwo)

    pygame.display.flip() 

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))
    print(degreeRotatedCarOne, degreeRotatedCarTwo)

pygame.quit() 