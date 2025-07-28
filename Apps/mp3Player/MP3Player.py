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


# for recieving over a socket (using pickle)
# with open("temp_song.mp3", "wb") as f:         opens file, writes in binary mode, assigns file to f
#     f.write(received_mp3_data)                 writes the recieved mp3 to the file

# pygame.mixer.music.load("temp_song.mp3")       loads the mp3
# pygame.mixer.music.play()                      plays the mp3


import pygame
import threading
import time

pygame.init()

screen = pygame.display.set_mode((500, 350))

songs = [
    {
        'Name': 'Gorillaz - Feel Good Inc.',
        'Path': r'Apps\mp3Player\Gorillaz - Feel Good Inc. (Official Video).mp3'
    }
]

run_timer = True
current_time = 0.0

class setImgs():
    def __init__(self, x, y, w, h, istransparent, colortoignorefortransparency, imgRaw):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.istransparent = istransparent
        self.colortoignorefortransparency = colortoignorefortransparency
        self.imgRaw = imgRaw
    def make_img(self):
        img = pygame.image.load(self.imgRaw).convert()
        if self.istransparent:
            img.set_colorkey(self.colortoignorefortransparency)
            print(self.colortoignorefortransparency)
        img = pygame.transform.scale(img, (self.w, self.h))
        return img

def track_song_progress():
    global current_time, song_playing
    while run_timer:
        if song_playing:
            time.sleep(0.1)
            current_time += 0.1
            print(f"Track Run Time: {current_time}s")
        else:
            time.sleep(0.05)

play_button = setImgs(225, 300, 50, 50, True, (255, 255, 255), r'Apps\mp3Player\play button.png')
play_button_img = play_button.make_img()

pause_button = setImgs(225, 300, 50, 50, True, (255, 255, 255), r'Apps\mp3Player\pause button.png')
pause_button_img = pause_button.make_img()

rewind_button = setImgs(175, 300, 50, 50, True, (255, 255, 255), r'Apps\mp3Player\rewind button.png')
rewind_button_img = rewind_button.make_img()

play_pause_button_status = 'Play'

song_playing = False
song_started = False

progress_thread = threading.Thread(target=track_song_progress, daemon=True)
progress_thread.start()

running = True
while running:
    mpos = pygame.mouse.get_pos()
    mouseButtonDown = False
    spaceButtonDown = False

    ################################################################################
    # EVENT HANDLEING
    ################################################################################

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonDown = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceButtonDown = True

    ################################################################################
    # HITBOXES FOR ICONS
    ################################################################################

    play_pause_button_hitbox = pygame.Rect(play_button.x, play_button.y, play_button_img.get_width(), play_button_img.get_height())
    rewind_button_hitbox = pygame.Rect(rewind_button.x, rewind_button.y, rewind_button_img.get_width(), rewind_button_img.get_height())


    ################################################################################
    # BLITING
    ################################################################################


    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(0, 275, 500, 275))

    if play_pause_button_status == 'Play':
        screen.blit(play_button_img, (play_button.x, play_button.y))
    else:
        screen.blit(pause_button_img, (pause_button.x, pause_button.y))

    screen.blit(rewind_button_img, (rewind_button.x, rewind_button.y))

    ################################################################################
    # COLLISION DETECTION
    ################################################################################

    m_collision_with_play_pause = play_pause_button_hitbox.collidepoint(mpos)
    m_collision_with_rewind = rewind_button_hitbox.collidepoint(mpos)

    ################################################################################
    # IF LOOP MAYHEM (FIGURING OUT WHAT BUTTON WAS PRESSED)
    ################################################################################

    ####################### Collision With Play/Pause Button #######################

    if (m_collision_with_play_pause and mouseButtonDown) or (spaceButtonDown):
        if not song_started and not song_playing:
            pygame.mixer.music.load(songs[0]['Path'])
            pygame.mixer.music.play()
            song_playing = True
            song_started = True
            play_pause_button_status = 'Pause'
        elif song_playing:
            pygame.mixer.music.pause()
            song_playing = False
            play_pause_button_status = 'Play'
        elif not song_playing and song_started:
            pygame.mixer.music.unpause()
            song_playing = True
            play_pause_button_status = 'Pause'

    ######################### Collision With Rewind Button #########################

    elif m_collision_with_rewind and mouseButtonDown:
        pygame.mixer.music.play(start=0)
        current_time = 0.0
        if song_playing == False:
            pygame.mixer.music.pause()

    ################################################################################
    # UPDATE SCREEN
    ################################################################################

    pygame.display.flip()

pygame.quit()