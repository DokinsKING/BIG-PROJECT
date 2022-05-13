import pygame
import cv2
import os
from random import randrange, choice
import sys
# import menu

#часть Саидаги
from food import Food 
from sword import Sword
import time
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
    #выключили отображение мыши
    pygame.mouse.set_visible(False)


    all_good = False
    real_coords = 0

    sw = Sword(screen)
    fd = pygame.sprite.Group()
    
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
        #разные вариации отображения количества фруктов
        if score == 1:
            score_t = f.render(f'Вы лопнули {score} фрукт',True,'white')
        elif '1' in str(score)[1::] and '11' not in str(score):
            score_t = f.render(f'Вы лопнули {score} фрукт',True,'white')
        elif 2 <= score <= 4:
            score_t = f.render(f'Вы лопнули {score} фрукта',True,'white')
        elif '2' in str(score)[1::] or '3' in str(score)[1::] or '4' in str(score)[1::] and '12' not in str(score) and '13' not in str(score) and '14' not in str(score):
            score_t = f.render(f'Вы лопнули {score} фрукта',True,'white')
        else:
            score_t = f.render(f'Вы лопнули {score} фруктов',True,'white')

        if len(fd) <= 10:
            fd.add(Food(screen,size))

        gotit = pygame.sprite.groupcollide(sw.sw, fd, False, False)
        
            

        #при сталкновении групп спрайтов начинатеся реакция
        if gotit:
            for item in gotit.items():
                item[1][0].was = True
        for i in fd:
            if i.score_plus == 1:
                poof.play()
                score += i.score_plus
        
        
        screen.fill('black')
        if all_good == False:
            pygame.draw.rect(screen,'blue',(0,0,size[0],size[1]))
            pygame.display.flip()

            answer = laser.tracking_rect()
            real_coords = answer[0]
            all_good = answer[1]
            # all_good = True

            

        elif all_good == True:
            # menu.menu()
            result_img = laser.transform_rect(real_coords,size)
            laser_coord = laser.cycle_laser(result_img)
            sw.sword_positions(laser_coord)
            # sw.sword_positions('Привет')

            fd.update()
            fd.draw(screen)
            screen.blit(score_t, (100,100))

            pygame.display.flip()
            clock.tick(FPS)
    pygame.quit()