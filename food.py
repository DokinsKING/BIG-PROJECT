import pygame
import os
from random import randrange, choice
import sys
sys.setrecursionlimit(10000)


def load_image(name, color_key=None):
    fullname = os.path.join('samples', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image




class Food():
    apple = pygame.transform.scale(load_image('foods\\red_apple.png'), (80,80))
    pear = pygame.transform.scale(load_image('foods\\pear.png'), (80,80))
    
    def __init__(self,screen):
        self.screen = screen
        self.fd = pygame.sprite.Group()

        self.variables = {}
        self.mx = []

    def new_object(self):
        if len(self.mx) <= 5:
            type = randrange(1,4)
            if type == 1:
                b = False
                f1r = randrange(300,801)
                f2r = randrange(350,400)
                rside = choice([-1.5,1.5,0])
                num = randrange(1,150)
                name = f'apple{num}'

                for n in range(len(self.mx)):
                    if f1r < self.mx[n][1] + 40 and f1r > self.mx[n][1] - 40:
                        b = True
                if not b and name not in self.variables:
                    self.variables[name] = pygame.sprite.Sprite()
                    self.variables[name].image = Food.apple
                    self.variables[name].rect = self.variables[name].image.get_rect()
                    self.variables[name].mask = pygame.mask.from_surface(self.variables[name].image)
                    self.variables[name].rect.x = f1r
                    self.variables[name].rect.y = 1000
                    self.mx.append(['a',f2r,10,rside,name])
                    self.fd.add(self.variables[name])
            elif type == 2:
                b = False
                f1r = randrange(300,801)
                f2r = randrange(350,400)
                rside = choice([-1.5,1.5,0])
                num1 = randrange(1,150)
                name = f'pear{num1}'

                for n in range(len(self.mx)):
                    if f1r < self.mx[n][1] + 40 and f1r > self.mx[n][1] - 40:
                        b = True
                if not b and name not in self.variables:
                    self.variables[name] = pygame.sprite.Sprite()
                    self.variables[name].image = Food.pear
                    self.variables[name].rect = self.variables[name].image.get_rect()
                    self.variables[name].mask = pygame.mask.from_surface(self.variables[name].image)
                    self.variables[name].rect.x = f1r
                    self.variables[name].rect.y = 1000
                    self.mx.append(['p',f2r,10,rside,name])
                    self.fd.add(self.variables[name])
            # elif type == 3:
            #     b = False
            #     f1r = randrange(300,801)
            #     f2r = randrange(350,400)
            #     rside = choice([-1.5,1.5,0])
            #     for n in range(len(self.mx)):
            #         if f1r < self.mx[n][1] + 40 and f1r > self.mx[n][1] - 40:
            #             b = True
            #     if not b:
            #         self.mx.append(['c',f1r,1000,f2r,10,rside])
    def spawning(self):
        for n in range(len(self.mx)):
            try:
                if self.mx[n][0] == 'a':
                    name = self.mx[n][4]
                    self.variables[name].rect.y -= self.mx[n][2]
                    self.variables[name].rect.x += self.mx[n][3]
                    if self.variables[name].rect.y < self.mx[n][1] + 100:
                        self.mx[n][2] -= 0.5
                    if self.variables[name].rect.y > 1000:
                        self.variables[name].kill()
                        del self.mx[n]
                    self.fd.draw(screen)
                if self.mx[n][0] == 'p':
                    name = self.mx[n][4]
                    self.variables[name].rect.y -= self.mx[n][2]
                    self.variables[name].rect.x += self.mx[n][3]
                    if self.variables[name].rect.y < self.mx[n][1] + 100:
                        self.mx[n][2] -= 0.5
                    if self.variables[name].rect.y > 1000:
                        self.variables[name].kill()
                        del self.mx[n]
                    self.fd.draw(screen)
            except IndexError:
                pass


def mouse_reaction():
    mouse = pygame.mouse.get_pos()
    print(mouse)




if __name__ == '__main__':
    pygame.init()
    size = width,height = 1080,900
    screen = pygame.display.set_mode(size)
    running = True
    pygame.display.flip()
    clock = pygame.time.Clock()
    FPS = 60

    fd = Food(screen)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mouse_reaction()

        screen.fill('black')
        fd.new_object()
        fd.spawning()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
