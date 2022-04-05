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
    pygame.init()
    size = width,height = 1080,900
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    FPS = 60
    #выключил отображение мыши
    pygame.mouse.set_visible(False)

    sw = Sword(screen)
    fd = Food(screen)

    #инициализация laser_tracker
    laser = LaserTracker()




    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #при сталкновении начинатеся реакция
        for m in fd.fd:
            if pygame.sprite.collide_mask(sw.sprite, m):
                for index, item in enumerate(fd.variables):
                    if str(item) == m.name:
                        del fd.mx[index]
                del fd.variables[str(m.name)]
                m.kill()


        screen.fill('black')
        sw.sword_positions(laser.cycle_laser())
        fd.new_object()
        fd.spawning()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()