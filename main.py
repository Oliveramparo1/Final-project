import pygame

pygame.init()
Screen_weigh = 1000
Screen_high = 900
screen = pygame.display.set_mode((Screen_weigh, Screen_high))
imgs_right = [pygame.image.load("Run_000.png"), pygame.image.load("Run_001.png"), pygame.image.load("Run_002.png"),
              pygame.image.load("Run_003.png"), pygame.image.load("Run_004.png"), pygame.image.load("Run_005.png"),
              pygame.image.load("Run_006.png"), pygame.image.load("Run_007.png"), pygame.image.load("Run_009.png"),
              pygame.image.load("Run_010.png"), pygame.image.load("Run_011.png")]


pygame.display.set_caption("Running")
w_count = 0
x_back = 200
x = 0
y = 200
velocity = 50

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
        self.j_count = 15
        self.w_count = 0
        self.direction = 1


    def draw(self, screen):
        if self.w_count + 1 >= 11:
            self.w_count = 0
        elif self.r_run:
            screen.blit(imgs_right[self.w_count // 1], (self.x, self.y))
            self.w_count += 1
        elif self.l_run:
            screen.blit(imgs_right[self.w_count // 1], (self.x, self.y))
            self.w_count += 1
        else:
            screen.blit(char, (self.x, self.y))



ene_right = pygame.image.load("enemy.png")


char = pygame.image.load("idle_000.png")

clock = pygame.time.Clock()


def wind():
    global x
    back = pygame.image.load("back1.png").convert()
    screen.blit(back, (x, -285))
    x = x -1
    mainc.draw(screen)

    pygame.display.update()
def block():
    green = 0, 255, 0
    pygame.draw.rect(screen, green, [300, 300, 200, 250])

def background():
    global x_back, Screen_weigh
    green = 0, 255, 0
    x2 = 900
    pygame.draw.rect(screen, green, [0, 400, x2, 400])
    while mainc.x > Screen_weigh/4:
        Screen_weigh += 10
        mainc.x = mainc.x - abs(mainc.velocity)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        green = 0, 255, 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



def enemy(x, y):
    global w_count

    if w_count + 1 >= 11:
        w_count = 0
        screen.blit(imgs_right[w_count // 1], (x, y))
        w_count += 1


mainc = main_character(100, 200, 400, 385)
main = True
while main:
    clock.tick(11)
    pygame.time.delay(25)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            main = False
    Platform(200, 250, 100, 40)
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
        mainc.y += 50
    block()
pygame.quit()
