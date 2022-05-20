import pygame
import cv2
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

class Menu():
    def __init__(self,screen,size):
        self.screen = screen
        self.size = size
        self.mn = pygame.display.set_mode(self.size)
        self.fruits = pygame.sprite.Group()
        self.mn_r = False
    def logo_sp(self):
        self.logo = pygame.transform.scale(load_image('logo.png'), (800, 430))
        self.mn.blit(self.logo, (round(self.size[0]//2-390), round(self.size[1]//100)))
    def buttons(self):
        self.fontsgame = pygame.font.Font(None, 100)
        self.starttext = self.fontsgame.render('Играть!', False, 'dark grey')
        self.exittext = self.fontsgame.render('Выход', False, 'dark grey')

        self.startbutton = pygame.draw.rect(self.mn, 'grey', (round(self.size[0]//2-200), round(self.size[1]//2), 400, 100), 10, 30)
        self.exitbutton = pygame.draw.rect(self.mn, 'grey', (round(self.size[0]//2-200), round(self.size[1]//2+200), 400, 100), 10, 30)

        self.mn.blit(self.starttext, (round(self.size[0]//2-124), round(self.size[1]//2+15)))
        self.mn.blit(self.exittext, (round(self.size[0]//2-124), round(self.size[1]//2+215)))
    def main(self):
        self.screen.blit(self.mn,(0,0))
        self.mn.fill('light blue')
        self.buttons()
        self.logo_sp()
        pygame.display.flip()
