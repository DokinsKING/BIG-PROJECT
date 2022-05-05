import pygame
import cv2
import os
from random import randrange, choice
import sys
import menu

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
    print(size)
    clock = pygame.time.Clock()
    FPS = 60
    score = 0
    poof = pygame.mixer.Sound('samples/sound/poof.mp3')
    #выключил отображение мыши
    pygame.mouse.set_visible(False)


    all_good = False
    real_coords = 0

    sw = Sword(screen)
    fd = Food(screen,size)
    
    f = pygame.font.Font(None, 36)

    #инициализация laser_tracker
    laser = LaserTracker()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if score == 1:
            score_t = f.render(f'Вы лопнули {score} фрукт',True,'white')
        elif 2 <= score <= 4:
            score_t = f.render(f'Вы лопнули {score} фрукта',True,'white')
        else:
            score_t = f.render(f'Вы лопнули {score} фруктов',True,'white')

        #при сталкновении начинатеся реакция
        for m in fd.fd:
            if pygame.sprite.collide_mask(sw.sprite, m):
                for index, item in enumerate(fd.variables):
                    if str(item) == m.name:
                        del fd.mx[index]
                del fd.variables[str(m.name)]
                m.kill()
                poof.play()
                score += 1
        

        #для эрнеста
        # food_coords = fd.limusin
        # print(food_coords)
        food_coords = fd.coords
        
        
        screen.fill('black')
        if all_good == False:
            
            pygame.draw.rect(screen,'blue',(0,0,size[0],size[1]))
            pygame.display.flip()
            answer = laser.tracking_rect()
            real_coords = answer[0]
            all_good = answer[1]

            

        elif all_good == True:
            menu.menu()
            result_img = laser.transform_rect(real_coords,size)
            laser_coord = laser.cycle_laser(result_img)
            sw.sword_positions(laser_coord)

            # fd.one_fruit()
            fd.new_object()
            fd.spawning()
            
            pygame.display.flip()
            clock.tick(FPS)
    pygame.quit()