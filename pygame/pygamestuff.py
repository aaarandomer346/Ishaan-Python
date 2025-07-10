import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640)) # makes a screen

# use for transparent images
potato_img = pygame.image.load('pygame\Potato_JE2.png').convert_alpha() # makes an image surface
# if the image is not transparent but has a solid color as the background:
# img.set_colorkey((0, 0, 0)) # change (0, 0, 0) to the code for the color you want to ignore

potato_img = pygame.transform.scale(potato_img,
                                    (64, # divide surface height by 2
                                     64)) # divide surface width by 2

# potatoes = pygame.Surface((200, 200), pygame.SRCALPHA)        can add multiple surfaces to a single surface
# potatoes.blit(potato_img, (0, 0))
# potatoes.blit(potato_img, (25, 0))
# potatoes.blit(potato_img, (12, 12))

running = True
x = 0
clock = pygame.time.Clock()

delta_time = 0.1

font = pygame.font.Font(None, size=30) # creates a text surface, by default has transparent background

moving = False

# for adding sound:
# sound = pygame.mixer.Sound('file_name.filetype')
# sound.play()

while running:
    screen.fill((255, 255, 255))

    # potatoes.set_alpha(max(0, 255 - x))    # fades out the img
    screen.blit(potato_img, (x, 30)) # adds to the screen

    hitbox = pygame.Rect(x, 30, potato_img.get_width(), potato_img.get_height())

    mpos = pygame.mouse.get_pos()

    target = pygame.Rect(300, 0, 160, 280)
    collision = hitbox.colliderect(target)
    m_collision = target.collidepoint(mpos)
    pygame.draw.rect(screen, (255 * collision, 255 * m_collision, 0), target)

    if moving == True:
        x += 50 * delta_time

    text = font.render('Hello world!', True, (0, 0, 0))
    screen.blit(text, (x / 2, 320))

    for event in pygame.event.get(): # for each event in a pygame event
        if event.type == pygame.QUIT: # if the pygame event is closing the winodw
            running = False # stop the while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving = False

    pygame.display.flip() # updates the display

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit() # close the program