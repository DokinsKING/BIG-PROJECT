import pygame
import os
from random import randrange

def load_image(name, color_key=None):
    fullname = os.path.join('DokinsKING version\samples', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
            return image
        else:
            image = image.convert_alpha()
            return image




class Food():
    # image = load_image('penguin\Idle\Armature_IDLE_00.png',-1)
    def __init__(self):
        # self.screen = 'pass'
        # self.fd = pygame.sprite.Group()

        # self.sprite = pygame.sprite.Sprite()
        # self.sprite.image = Food.image
        # self.sprite.rect = self.sprite.image.get_rect()
        # self.fd.add(self.sprite)
        self.mx = []

    def spawning(self):
        if len(self.mx) <= 6:
            type = randrange(1,4)
            if type == 1:
                self.mx.append(['r',randrange(300,801),1000,randrange(350,400),True])
            elif type == 2:
                self.mx.append(['c',randrange(300,801),1000,randrange(350,400),True])
            elif type == 3:
                self.mx.append(['c',randrange(300,801),1000,randrange(350,400),True])
        for n in range(len(self.mx)):
            try:
                if self.mx[n][0] == 'r':
                    if self.mx[n][4] == True:
                        self.mx[n][2] -= 3
                        if self.mx[n][2] < self.mx[n][3]:
                            self.mx[n][4] = False
                    elif self.mx[n][4] == False:
                        self.mx[n][4] = False
                        self.mx[n][2] += 4
                        if self.mx[n][2] > 1000:
                            del self.mx[n]
                    pygame.draw.rect(screen,'red',(self.mx[n][1],self.mx[n][2],40,40))
                if self.mx[n][0] == 'c':
                    if self.mx[n][4] == True:
                        self.mx[n][2] -= 3
                        if self.mx[n][2] < self.mx[n][3]:
                            self.mx[n][4] = False
                    elif self.mx[n][4] == False:
                        self.mx[n][4] = False
                        self.mx[n][2] += 4
                        if self.mx[n][2] > 1000:
                            del self.mx[n]
                    pygame.draw.circle(screen,'yellow',(self.mx[n][1],self.mx[n][2]),20)
            except IndexError:
                pass



fd = Food()



if __name__ == '__main__':
    pygame.init()
    size = width,height = 1080,900
    screen = pygame.display.set_mode(size)
    running = True
    pygame.display.flip()
    clock = pygame.time.Clock()
    FPS = 120

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill('black')
        fd.spawning()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
