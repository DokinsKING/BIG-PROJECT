#загрузка изображения игрока
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

class Sword():
        image = load_image('penguin\Idle\Armature_IDLE_00.png',-1)
        def __init__(self,world):
            self.world = world
            self.eng = pygame.sprite.Group()

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = pygame.transform.scale(Enemy.image,(90,90))
            self.sprite.rect = self.sprite.image.get_rect()
            self.eng.add(self.sprite)

        def spawning(self):
            for i in range(len(map)):
                for z in range(len(map[i])):
                    if map[i][z] == 'E':
                        self.sprite.rect.x = z * 90
                        self.sprite.rect.y = i * 90
                        self.eng.draw(self.world)
