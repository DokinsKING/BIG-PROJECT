import pygame
import os
from random import randrange, choice
import sys

#часть Саидаги
from food import Food 
from sword import Sword

#часть Эрнеста
from laser_tracker import LaserTracker

 
if __name__ == '__main__':
    #инициализация pygame
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    size = screen.get_size()
    clock = pygame.time.Clock()
    FPS = 60
    pygame.mixer.music.load('samples\sound\poof.mp3')
    #выключил отображение мыши
    pygame.mouse.set_visible(False)

    sw = Sword(screen)
    fd = Food(screen,size)
    

    #инициализация laser_tracker
    laser = LaserTracker()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        #при сталкновении начинатеся реакция
        for m in fd.fd:
            if pygame.sprite.collide_mask(sw.sprite, m):
                for index, item in enumerate(fd.variables):
                    if str(item) == m.name:
                        del fd.mx[index]
                del fd.variables[str(m.name)]
                m.kill()
                pygame.mixer.music.play()

        screen.fill('black')
        pygame.draw.circle(screen,'white',(13,13),10)
        pygame.draw.circle(screen,'purple',(size[0] - 13,13),10)
        pygame.draw.circle(screen,'blue',(13,size[1] - 13),10)
        pygame.draw.circle(screen,'pink',(size[0] - 13,size[1] - 13),10)
        # sw.sword_positions(laser.cycle_laser())
        fd.new_object()
        fd.spawning()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()