import pygame
import os
from random import randrange, choice
import sys

#загрузка изображения игрока
def load_image(name, color_key=None):
    fullname = os.path.join('samples', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image

class Sword():
        image = load_image('sword\\aim.png')
        image = pygame.transform.scale(image, (200,200))
        def __init__(self,screen):
            #тоже самое, что и в фуд
            self.screen = screen
            self.sw = pygame.sprite.Group()
            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = Sword.image
            self.sprite.rect = self.sprite.image.get_rect()
            self.sprite.mask = pygame.mask.from_surface(self.sprite.image)
            self.sw.add(self.sprite)

        def sword_positions(self, coord):
            #координаты мыши
            mouse = pygame.mouse.get_pos()
            #ставлю мышь в середину спрайт
            if coord == ['Привет']:
                self.sprite.rect.x = mouse[0] - self.sprite.image.get_rect()[2]/2
                self.sprite.rect.y = mouse[1] - self.sprite.image.get_rect()[3]/2
                self.sw.draw(self.screen)
            else:
                self.sprite.rect.x = coord[0] - self.sprite.image.get_rect()[2]/2
                self.sprite.rect.y = coord[1] - self.sprite.image.get_rect()[3]/2
                self.sw.draw(self.screen)

