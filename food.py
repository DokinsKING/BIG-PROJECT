from re import S
import pygame
import os
from random import randrange, choice
import sys

def load_image(name, color_key=None):
    fullname = os.path.join('samples', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image

apple = pygame.transform.scale(load_image('foods/red_apple.png'), (80,80))
pear = pygame.transform.scale(load_image('foods/pear.png'), (80,80))


class Food(pygame.sprite.Sprite):  
    def __init__(self,screen,size):
        super().__init__()

        type = randrange(1,3)

        if type == 1:
            self.image = apple
        elif type == 2:
            self.image = pear

        self.screen = screen
        self.size = size
        self.rect = self.image.get_rect()
        self.rect.x = randrange(500,self.size[0] - 500)
        self.rect.y = self.size[1] + 200
        self.maxheight = randrange(round(self.size[1]/3),round(self.size[1]/2))
        self.gravity = 10
        self.sidex = choice([-1.5,1.5,0])
        

    def update(self):
        self.rect.y -= self.gravity
        self.rect.x += self.sidex
        #это типо гравитация и чем выше тем медленнне летит спрайт, потом уже вниз
        if self.rect.y < self.maxheight + 100:
            self.gravity -= 0.5
        #когда спрайт улетит вниз, то поменяет координаты и поднимется уже с друго места
        if self.rect.y > self.size[1] + 200:
            self.rect.y = self.size[1] + 200
            self.rect.x = randrange(500,self.size[0] - 500)
            self.maxheight = randrange(round(self.size[1]/3),round(self.size[1]/2))
            self.gravity = 10
            self.sidex = choice([-1.5,1.5,0])
