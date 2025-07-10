# Features:

# 1. Being able to play a mp3 file, skip to next mp3 file, go to previous mp3 file
# 2. being able to add a song to a file and then playing that select song
#       a. able to set a title and cover image
# 3. list of songs
# 4. search for a song

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 350))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()