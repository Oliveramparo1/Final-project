import pygame

pygame.init()

weigh = 800
high = 500
pygame.display.set_mode((weigh, high))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.loud('Run(1).png')



if __name__ == "__main__":
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            main = False
    pygame.display.update()

