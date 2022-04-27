import pygame, os
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
#------------------------------------------------
#------------------------------------------------
#Ввод логотипа и кнопок
def logo():

    logo = pygame.transform.scale(load_image('logo.png'), (800, 430))
    menu_screen.blit(logo, (300, 5))

def buttons():
    global startbutton, exitbutton

    startbutton = pygame.draw.rect(menu_screen, 'blue', (500, 300, 400, 300), 0)
    exitbutton = pygame.draw.rect(menu_screen, 'blue', (500, 300, 400, 300), 0)

def set_menu():
    global menu_screen

    menu_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    return menu_screen
#------------------------------------------------
#------------------------------------------------
#Класс экрана
class Screen(pygame.Surface):
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.size = self.screen.get_size()

    def screen_blit(self, screen):
        self.screen.blit(screen, (0, 0))

    def clean(self):
        self.screen.fill('BLACK')
        pygame.display.flip()

#------------------------------------------------
#------------------------------------------------
#Фрукты
class Food_m():
    #загружаем изображение еды
    apple = pygame.transform.scale(load_image('foods/red_apple.png'), (80,80))
    pear = pygame.transform.scale(load_image('foods/pear.png'), (80,80))
    
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
        if len(self.mx) <= 50:
            #рандомно выбираю какая еда заспавнится
            type = randrange(1,4)
            #смотря какой тип будет появлятся еда
            if type == 1:
                #рандомно выбираю координату x
                f1r = randrange(0,self.size[0] - 500)
                f2r = randrange(-3000,-150)
                #создаю рандомное имя для спрайта
                num = randrange(1,150)
                name = f'apple{num}'

                for i in range(len(self.mx)):
                    if self.variables[self.mx[i][1]].rect.x > f1r - 100 and self.variables[self.mx[i][1]].rect.x < f1r + 100:
                        break

                if name not in self.variables:
                    #создаю спрайт и задаю ему все параметры
                    self.variables[name] = pygame.sprite.Sprite()
                    self.variables[name].image = Food_m.apple
                    self.variables[name].rect = self.variables[name].image.get_rect()
                    self.variables[name].mask = pygame.mask.from_surface(self.variables[name].image)
                    self.variables[name].name = name
                    self.variables[name].rect.x = f1r
                    self.variables[name].rect.y = f2r
                    self.mx.append(['a',name])
                    self.fd.add(self.variables[name])
            #тут тоже самое, что и с типом 1
            elif type == 2:
                f1r = randrange(15,self.size[0] - 500)
                f2r = randrange(-3000,-150)
                num1 = randrange(1,150)
                name = f'pear{num1}'


                for i in range(len(self.mx)):
                    if self.variables[self.mx[i][1]].rect.x > f1r - 100 and self.variables[self.mx[i][1]].rect.x < f1r + 100:
                        break

                if name not in self.variables:
                    self.variables[name] = pygame.sprite.Sprite()
                    self.variables[name].image = Food_m.pear
                    self.variables[name].rect = self.variables[name].image.get_rect()
                    self.variables[name].mask = pygame.mask.from_surface(self.variables[name].image)
                    self.variables[name].name = name
                    self.variables[name].rect.x = f1r
                    self.variables[name].rect.y = f2r
                    self.mx.append(['p',name])
                    self.fd.add(self.variables[name])
    def spawning(self):
        for n in range(len(self.mx)):
            try:
                #если параметр а-apple то создаем яблоко
                if self.mx[n][0] == 'a':
                    #смотрю какое имя у этого спрайта
                    name = self.mx[n][1]
                    #работа с координатами спрайта
                    self.variables[name].rect.y += 5
                    #когда спрайт улетит вниз, то удалится
                    if self.variables[name].rect.y > self.size[1] + 200:
                        self.variables[name].kill()
                        del self.variables[name]
                        del self.mx[n]
                    self.fd.draw(self.screen)
                #тоже самое что и сверху
                if self.mx[n][0] == 'p':
                    name = self.mx[n][1]
                    self.variables[name].rect.y += 5
                    if self.variables[name].rect.y > self.size[1] + 200:
                        self.variables[name].kill()
                        del self.variables[name]
                        del self.mx[n]
                    self.fd.draw(self.screen)
            except IndexError:
                pass
            except KeyError:
                pass
#------------------------------------------------
#------------------------------------------------
#Основной цикл
main_screen = Screen()
main_screen.screen_blit(set_menu())

def main():
    global main_screen
    pygame.init()
    running = True

    

    fruit = Food_m(main_screen.screen,main_screen.size)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        main_screen.screen.fill('light blue')
        buttons()
        fruit.new_object()
        fruit.spawning()
        logo()
        pygame.display.flip()
        

main()