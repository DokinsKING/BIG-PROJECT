import pygame
import os
from random import randrange

def load_image(name, color_key=None):
    fullname = os.path.join('DokinsKING version\samples', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
            return image
        else:
            image = image.convert_alpha()
            return image




class Food():
    # image = load_image('penguin\Idle\Armature_IDLE_00.png',-1)
    def __init__(self):
        # self.screen = 'pass'
        # self.fd = pygame.sprite.Group()

        # self.sprite = pygame.sprite.Sprite()
        # self.sprite.image = Food.image
        # self.sprite.rect = self.sprite.image.get_rect()
        # self.fd.add(self.sprite)
        pass

    def spawning(self):
        type = randrange(1,4)
        print(type)


fd = Food()

fd.spawning()



if __name__ == '__main__':
    pygame.init()
    size = width,height = 501,501
    screen = pygame.display.set_mode(size)
    running = True
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0,0,0))
        pygame.display.flip()
    pygame.quit()