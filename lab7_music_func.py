import pygame
import os
def next(music, x):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load(music[x])
    pygame.mixer.music.play(0)
def previous(music, x):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(music[x])
        pygame.mixer.music.play(0)
    except:
        print("problems with PREVIOUS")

def stop(music):
    try:
        pygame.mixer.music.stop()
    except:
        print("problems with STOP")
def play(music, x):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    except:
        print("problems with PLAY")
    pygame.mixer.music.load(music[x])
    pygame.mixer.music.play(0)
def b_up(screen):
    color = (0, 0, 0)
    height = screen.get_height()/5
    width = screen.get_width()
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render('Play', True, color)
    #screen.blit(text, (0, 0))
    screen.blit(text, (250 - text.get_width() // 2, 75 - text.get_height() // 2 + 5))
def b_down(screen):
    color = (0, 0, 0)
    height = screen.get_height()/5
    width = screen.get_width()
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render('Stop', True, color)
    #screen.blit(text, (0, 0))
    screen.blit(text, (250 - text.get_width() // 2, 75 - text.get_height() // 2 + 90))
def b_left(screen):
    color = (0, 0, 0)
    height = screen.get_height()/5
    width = screen.get_width()
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render('Previous', True, color)
    #screen.blit(text, (0, 0))
    screen.blit(text, (250 - text.get_width() // 2, 75 - text.get_height() // 2 + 270))
def b_right(screen):
    color = (0, 0, 0)
    height = screen.get_height()/5
    width = screen.get_width()
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render('Next', True, color)
    #screen.blit(text, (0, 0))
    screen.blit(text, (250 - text.get_width() // 2, 75 - text.get_height() // 2 + 180))
def draw(screen):
    pygame.draw.line(screen, (0, 0, 153), (135, 50), (135, 365), 10)
    pygame.draw.polygon(screen, (128, 128, 128), [(60, 50), (60, 100), (85, 75)])
    pygame.draw.line(screen, (128, 128, 128), (60, 140), (60, 190), 10)
    pygame.draw.line(screen, (128, 128, 128), (80, 140), (80, 190), 10)
    pygame.draw.line(screen, (128, 128, 128), (50, 250), (80, 250), 10)
    pygame.draw.polygon(screen, (128, 128, 128), [(80, 225), (80, 275), (105, 250)])
    pygame.draw.line(screen, (128, 128, 128), (75, 340), (105, 340), 10)
    pygame.draw.polygon(screen, (128, 128, 128), [(75, 315), (75, 365), (50, 340)])