# Features:

# spotify clone bassically
# run a server that stores mp3s that users can upload
# allow users to then search somewhere and based on if certain words in their phrase appear in a mp3:
# show the top 5 mp3s that match
    # use something where it shows the top 5 based on a percentage
    # the percentage works by what percent of the words match the words in the title
        # can level up to having tags if needed
# play the mp3

# also use .ogg instead of mp3, its better, and more supported

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 350))

play_button_img = pygame.image.load('Apps\mp3Player\play button.png').convert_alpha()
play_button_img.set_colorkey((0, 0, 0))
play_button_img = pygame.transform.scale(play_button_img,
                                    (50, # 50px
                                     50)) # by 50px
play_button_x = 225
play_button_y = 300

song = pygame.mixer.Sound('Apps\mp3Player\Gorillaz - Feel Good Inc. (Official Video).mp3')
song_playing = False
song_started = False

running = True
while running:
    mpos = pygame.mouse.get_pos()
    mouseButtonDown = False

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonDown = True

    play_button_hitbox = pygame.Rect(play_button_x, play_button_y, play_button_img.get_width(), play_button_img.get_height())
    screen.blit(play_button_img, (play_button_x, play_button_y))

    m_collision = play_button_hitbox.collidepoint(mpos)
    if m_collision and mouseButtonDown:
        if not song_started and not song_playing:
            curr_playing = song.play()
            song_playing = True
            song_started = True
        elif song_playing:
            curr_playing.pause()
            song_playing = False
        elif not song_playing and song_started:
            curr_playing.unpause()
            song_playing = True
    pygame.display.flip()

pygame.quit()