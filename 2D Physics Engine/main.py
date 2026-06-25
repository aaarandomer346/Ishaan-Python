import pygame

pygame.init()

screenX = 640
screenY = 640
screen = pygame.display.set_mode((screenX, screenY)) 

clock = pygame.time.Clock()

gravity = 0.5

delta_time = 0.1

class ball():
    def __init__(self, surface, color, x, y, size, velocity):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.velocity = velocity
    def makeCircle(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.size)
    def falling(self, gravity):
        addGravity = True
        # update velocity by gravity, add velocity to self.y, if hits the bottom then multiply velocity by -0.7

        if self.y + self.size <= screenY + 5 and addGravity == True:
            self.velocity += gravity    
        else:
            self.y = screenY - self.size
            self.velocity = self.velocity * -0.7

        if self.y >= screenY - self.size - 10 and 2.5 >= self.velocity >= -1:
            addGravity = False
            self.y = screenY - self.size
            self.velocity = 0
        
        self.y += self.velocity

circleOne = ball(screen, (255, 0, 255), 200, 50, 25, 0.1)
circleTne = ball(screen, (255, 0, 0), 250, 50, 25, 0.1)



running = True
while running:
    delta_time = clock.tick(60) / 1000.0  # convert to seconds
    delta_time = max(0.001, min(0.1, delta_time))


    print("Velocity: " + str(circleOne.velocity))
    print("Y: " + str(circleOne.y))
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if circleOne.y + circleOne.size != screenY:
        circleOne.falling(gravity)
        circleTne.falling(gravity)


    circleOne.makeCircle()
    circleTne.makeCircle()
    pygame.display.flip()

pygame.quit() 