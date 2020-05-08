import pygame

pygame.init()
Screen_weigh = 1000
Screen_high = 900
screen = pygame.display.set_mode((Screen_weigh, Screen_high))
imgs_right = [pygame.image.load("Run_000.png"), pygame.image.load("Run_001.png"), pygame.image.load("Run_002.png"),
              pygame.image.load("Run_003.png"), pygame.image.load("Run_004.png"), pygame.image.load("Run_005.png"),
              pygame.image.load("Run_006.png"), pygame.image.load("Run_007.png"), pygame.image.load("Run_009.png"),
              pygame.image.load("Run_010.png"), pygame.image.load("Run_011.png")]
ene_right = pygame.image.load("enemy.png")
pygame.display.set_caption("Running")
w_count = 0
x_back = 200
x = 0
y = 200
velocity = 50
enex = 600
eney = 300
ene_velocity = 30
enex += 10
screen.blit(ene_right, (400, 400))


class main_character():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 50
        self.jumping = False
        self.l_run = False
        self.r_run = False
        self.w_count = 0
        self.direction = 1

    def draw(self, screen):
        if self.w_count + 1 > 11:
            self.w_count = 0
        elif self.r_run:
            screen.blit(imgs_right[self.w_count // 1], (self.x, self.y))
            self.w_count += 1
        elif self.l_run:
            screen.blit(imgs_right[self.w_count // 1], (self.x, self.y))
            self.w_count += 1
        else:
            screen.blit(char, (self.x, self.y))


char = pygame.image.load("idle_000.png")

clock = pygame.time.Clock()


def wind():
    global x, y
    back = pygame.image.load("back3.png").convert()
    x_val2 = x % back.get_rect().width

    screen.blit(back, (x_val2 - back.get_rect().width, 700))
    x = x - 5
    if x_val2 < Screen_weigh:
        screen.blit(back, (x_val2, 700))
    mainc.draw(screen)

    pygame.display.update()


def block():
    green = 0, 255, 0
    pygame.draw.rect(screen, green, [300, 300, 200, 250])


def background():
    global x_back, Screen_weigh
    green = 0, 255, 0
    x2 = 900
    pygame.draw.rect(screen, green, [0, 300, x2, 400])
    while mainc.x > Screen_weigh / 4:
        Screen_weigh += 10
        mainc.x = mainc.x - mainc.velocity



mainc = main_character(100, 200, 400, 385)

main = True
while main:
    screen.fill((135, 206, 235))

    clock.tick(20)
    pygame.time.delay(25)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            main = False

    x_val = mainc.x
    y_val = mainc.y
    pla_col = pygame.Rect(x_val, y_val, 400, 385)
    plat = pygame.Rect(200, 200, 100, 50)
    pl = pygame.Rect(400, 200, 200, 50)
    if pla_col.colliderect(plat):

        pygame.draw.rect(screen, (255, 0, 0), plat)
    else:
        pygame.draw.rect(screen, (255, 0, 0), plat)

    if pla_col.colliderect(pl):

        pygame.draw.rect(screen, (255, 0, 0), pl)

    else:
        pygame.draw.rect(screen, (255, 0, 0), pl)

    wind()
    background()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_d]:
        mainc.x = mainc.x + mainc.velocity
        mainc.l_run = False
        mainc.r_run = True

    if key_pressed[pygame.K_a]:
        mainc.x = mainc.x - mainc.velocity
        mainc.l_run = True
        mainc.r_run = False

    if key_pressed[pygame.K_SPACE]:
        mainc.jumping = 300

    if mainc.jumping > 1:
        mainc.y -= mainc.velocity
        mainc.jumping -= mainc.velocity
    elif mainc.y < Screen_high - 500:
        if pla_col.colliderect(plat):

            pygame.draw.rect(screen, (0, 255, 0), plat)

        else:
            pygame.draw.rect(screen, (0, 255, 0), plat)
            mainc.y += 50


pygame.quit()
