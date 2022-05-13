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

# apple = pygame.transform.scale(load_image('foods/red_apple.png'), (80,80))
# pear = pygame.transform.scale(load_image('foods/pear.png'), (80,80))
apple = [load_image('foods\\A\\apple1.png'),load_image('foods\\A\\apple2.png'),load_image('foods\\A\\apple3.png'),
load_image('foods\\A\\apple4.png'),load_image('foods\\A\\apple5.png'),load_image('foods\\A\\apple6.png'),
load_image('foods\\A\\apple7.png'),load_image('foods\\A\\apple8.png'),load_image('foods\\A\\apple9.png'),load_image('foods\\A\\apple10.png'),]

lemon = [load_image('foods\\L\\lemon1.png'),load_image('foods\\L\\lemon2.png'),load_image('foods\\L\\lemon3.png'),
load_image('foods\\L\\lemon4.png'),load_image('foods\\L\\lemon5.png'),load_image('foods\\L\\lemon6.png'),
load_image('foods\\L\\lemon7.png'),load_image('foods\\L\\lemon8.png'),load_image('foods\\L\\lemon9.png'),load_image('foods\\L\\lemon10.png'),]

melon = [load_image('foods\\M\\melon1.png'),load_image('foods\\M\\melon2.png'),load_image('foods\\M\\melon3.png'),
load_image('foods\\M\\melon4.png'),load_image('foods\\M\\melon5.png'),load_image('foods\\M\\melon6.png'),
load_image('foods\\M\\melon7.png'),load_image('foods\\M\\melon8.png'),load_image('foods\\M\\melon9.png'),load_image('foods\\M\\melon10.png'),]


class Food(pygame.sprite.Sprite):  
    def __init__(self,screen,size):
        super().__init__()

        type = randrange(1,4)

        if type == 1:
            self.animlist = apple
            self.image = self.animlist[0]
        elif type == 2:
            self.animlist = lemon
            self.image = self.animlist[0]
        elif type == 3:
            self.animlist = melon
            self.image = self.animlist[0]

        self.screen = screen
        self.size = size
        self.rect = self.image.get_rect()
        self.rect.x = randrange(500,self.size[0] - 500)
        self.rect.y = self.size[1] + 200
        self.maxheight = randrange(round(self.size[1]/3),round(self.size[1]/2))
        self.gravity = 10
        self.sidex = choice([-1.5,1.5,0])


        self.was = False
        self.frame = 0
        self.score_plus = 0
        

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
        self.checking_was()

    def checking_was(self):
        if self.was == True:
            self.image = self.animlist[self.frame]
            self.frame += 1
            if self.frame > 8:
                self.score_plus = 1
            if self.frame > 9:
                self.kill()

