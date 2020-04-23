import pygame

pygame.init()
Screen_weigh = 900
Screen_high = 900
screen = pygame.display.set_mode((Screen_weigh, Screen_high))
imgs_right = [pygame.image.load("Run.png"), pygame.image.load("Run2.png"), pygame.image.load("Run3.png"),
              pygame.image.load("Run4.png"), pygame.image.load("Run5.png"), pygame.image.load("Run6.png"),
              pygame.image.load("Run7.png"), pygame.image.load("Run8.png")]
imgs_left = [pygame.image.load("Runleft.png"), pygame.image.load("Runleft2.png"), pygame.image.load("Run2.png")]

pygame.display.set_caption("Running")
x = 0
y = 200
velocity = 50
l_run = False
r_run = False
w_count = 0
back = pygame.image.load("back.jpg")
char = pygame.image.load("Idle1.png")

clock = pygame.time.Clock()


def wind():
    global w_count
    screen.blit(back, (0, 0))
    if w_count + 1 >= 9:
        w_count = 0
    if r_run:
        screen.blit(imgs_right[w_count // 1], (x, y))
        w_count += 1
    elif l_run:
        screen.blit(imgs_left[w_count // 1], (x, y))
        w_count += 1
    else:
        screen.blit(char, (x, y))
        w_count = 0

    pygame.display.update()


main = True
while main:
    pygame.time.delay(25)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            main = False
    clock.tick(9)
    wind()

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_d]:
        x = x + velocity
        l_run = False
        r_run = True
    elif key_pressed[pygame.K_a] and x > -100:
        x = x - velocity
        l_run = False
        r_run = True


    else:
        l_run = False
        r_run = False

pygame.quit()
