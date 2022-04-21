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




class Food():
    #загружаем изображение еды
    apple = pygame.transform.scale(load_image('foods\\red_apple.png'), (80,80))
    pear = pygame.transform.scale(load_image('foods\\pear.png'), (80,80))
    
    def __init__(self,screen,size):
        #получил скрин
        self.screen = screen
        #создал группу для спрайтов
        self.fd = pygame.sprite.Group()

        self.size = size
        
        #создал словарь, чтобы генерировать имена спрайтов
        self.variables = {}
        #создал список, там будут параметры каждого спрайта
        self.mx = []

    def new_object(self):
        if len(self.mx) <= 10:
            #рандомно выбираю какая еда заспавнится
            type = randrange(1,4)
            #смотря какой тип будет появлятся еда
            if type == 1:
                #рандомно выбираю координату x
                f1r = randrange(500,self.size[0] - 500)
                #рандомно выбираю максимальное высоту, на которую поднимится еда
                f2r = randrange(self.size[1]/3,self.size[1]/2)
                #рандомно выбираю в какую сторону полетит еда
                rside = choice([-1.5,1.5,0])
                #создаю рандомное имя для спрайта
                num = randrange(1,150)
                name = f'apple{num}'

                if name not in self.variables:
                    #создаю спрайт и задаю ему все параметры
                    self.variables[name] = pygame.sprite.Sprite()
                    self.variables[name].image = Food.apple
                    self.variables[name].rect = self.variables[name].image.get_rect()
                    self.variables[name].mask = pygame.mask.from_surface(self.variables[name].image)
                    self.variables[name].name = name
                    self.variables[name].rect.x = f1r
                    self.variables[name].rect.y = self.size[1] + 200
                    self.mx.append(['a',f2r,10,rside,name])
                    self.fd.add(self.variables[name])
            #тут тоже самое, что и с типом 1
            elif type == 2:
                f1r = randrange(500,self.size[0] - 500)
                f2r = randrange(self.size[1]/3,self.size[1]/2)
                rside = choice([-1.5,1.5,0])
                num1 = randrange(1,150)
                name = f'pear{num1}'

                for n in range(len(self.mx)):
                    if f1r < self.mx[n][1] + 40 and f1r > self.mx[n][1] - 40:
                        b = True
                if name not in self.variables:
                    self.variables[name] = pygame.sprite.Sprite()
                    self.variables[name].image = Food.pear
                    self.variables[name].rect = self.variables[name].image.get_rect()
                    self.variables[name].mask = pygame.mask.from_surface(self.variables[name].image)
                    self.variables[name].name = name
                    self.variables[name].rect.x = f1r
                    self.variables[name].rect.y = self.size[1] + 200
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
                #если параметр а-apple то создаем яблоко
                if self.mx[n][0] == 'a':
                    #смотрю какое имя у этого спрайта
                    name = self.mx[n][4]
                    #работа с координатами спрайта
                    self.variables[name].rect.y -= self.mx[n][2]
                    self.variables[name].rect.x += self.mx[n][3]
                    #это типо гравитация и чем выше тем медленнне литит спрайт, потом уже вниз
                    if self.variables[name].rect.y < self.mx[n][1] + 100:
                        self.mx[n][2] -= 0.5
                    #когда спрайт улетит вниз, то удалится
                    if self.variables[name].rect.y > self.size[1] + 200:
                        self.variables[name].kill()
                        del self.variables[name]
                        del self.mx[n]
                    self.fd.draw(self.screen)
                #тоже самое что и сверху
                if self.mx[n][0] == 'p':
                    name = self.mx[n][4]
                    self.variables[name].rect.y -= self.mx[n][2]
                    self.variables[name].rect.x += self.mx[n][3]
                    if self.variables[name].rect.y < self.mx[n][1] + 100:
                        self.mx[n][2] -= 0.5
                    if self.variables[name].rect.y > self.size[1] + 200:
                        self.variables[name].kill()
                        del self.variables[name]
                        del self.mx[n]
                    self.fd.draw(self.screen)
            except IndexError:
                pass
            except KeyError:
                pass



