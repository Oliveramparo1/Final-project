import pygame
import os

pygame.init()
Screen_weigh = 800
Screen_high = 500
screen = pygame.display.set_mode((Screen_weigh, Screen_high))
pygame.display.set_caption("Running")
x = 50
y = 400
width = 40
hight = 60
velocity = 5


def images():
    os.path.abspath('D:/Final-project/png')
    walkright = pygame.image.load('Run(1).png')


def movement():
    global x
    global y
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_d] and x < Screen_weigh - 40:
        x = x + velocity
    if key_pressed[pygame.K_a] and x > 0:
        x = x - velocity
    if key_pressed[pygame.K_w] and y > 0:
        y = y - velocity
    screen.fill((255, 0, 0))


thing = True
while thing:
    pygame.time.delay(100)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            thing = False
    movement()
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width, hight))
    pygame.display.update()
pygame.quit()
