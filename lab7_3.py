import random
import pygame
pygame.init()

# RGB (255, 255, 255)
#BLUE = (0, 0, 255)
#GREEN = (0, 255, 0)
#C = (100, 100, 100)
#BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)



size = width, height = (1440, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Program 3')
clock = pygame.time.Clock()  # FPS

color = RED

x = 300
y = 300

speed = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and x + speed < screen.get_width() - 20:
            x += speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and x - speed > 20:
            x -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and y - speed > 20:
            y -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and y + speed < screen.get_height() - 20:
            y += speed
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, color, [x, y, 25, 25])
    clock.tick(60)
    pygame.display.update()