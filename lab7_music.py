import pygame
import os
from lab7_music_func import *
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Program 2')
music = ['balkon.mp3', 'dance_of_knights.mp3', 'masks.mp3']
if music[0] is None:
    for i in music:
        i = i.replace('/', os.sep).replace('\\', os.sep)
x = 0
#pygame.mixer.music.load(music[x])
#pygame.mixer.music.play(0)
SONG_END = pygame.USEREVENT + 1

done = False
while not done:
    screen.fill((255, 255, 255))
    event = pygame.event.get()
    b_up(screen)
    b_down(screen)
    b_left(screen)
    b_right(screen)
    draw(screen)
    for i in event:
        if i == pygame.QUIT:
            stop(music)
            done = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                if x - 1 == -1:
                    x = len(music) - 1
                else:
                    x -= 1
                m = previous(music, x)
                print(x)
            elif i.key == pygame.K_RIGHT:
                if x + 1 == len(music):
                    x = 0
                else:
                    x += 1
                m = next(music, x)
                print(x)
            elif i.key == pygame.K_UP:
                m = play(music, x)
                print(x)
            elif i.key == pygame.K_DOWN:
                m = stop(music)
                print(x)
        if i.type == SONG_END:
            m = next(music, x)
            print(x)
    pygame.display.flip()