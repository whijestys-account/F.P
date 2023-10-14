from pygame import *
import pygame as pg

class GameSprite(sprite.Sprite):
    def __init__(self, name, x, y, speed, w=50, h=50):
        super().__init__()
        self.image = transform.scale(image.load(name), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.h = h
        self.w = w
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win_w = 700
win_h = 500
class Player(GameSprite):
    # def update(self):
    #     keys = key.get_pressed()
    #     if keys[K_LEFT] and self.rect.x > 5:
    #         self.rect.x -= self.speed
    #     if keys[K_RIGHT] and self.rect.x < win_w - self.w:
    #         self.rect.x += self.speed
    #     if keys[K_UP] and self.rect.y > 5:
    #         self.rect.y -= self.speed
    #     if keys[K_DOWN] and self.rect.y < win_h - self.h:
    #         self.rect.y += self.speed
    def move(self, pos):
        self.rect.x = pos.x
        self.rect.y = pos.y

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_w-self.w:
            self.direction = 'left'

        if self.direction == "left":
            self.rect.x -=self.speed
        else:
            self.rect.x +=self.speed
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wl_x, wl_y, wl_w, wl_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wl_w
        self.height = wl_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wl_x
        self.rect.y = wl_y

class Winn(sprite.Sprite):
    def __init__(self, color1, color2, color3, wl_x, wl_y, wl_w, wl_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wl_w
        self.height = wl_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wl_x
        self.rect.y = wl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
mixer.init()
mixer.music.load('LL.mp3')
mixer.music.play()

pos = pg.mouse.get_pos()
window = display.set_mode((win_w,win_h))
back = transform.scale(image.load('maxrjpg.jpg'), (win_w,win_h))
player = Player('NarCat.png', 50, 50, 5, 70,70)
enemy = Enemy('Jujment.png', 450, 250, 3, 90,90)
final = Winn(150, 0, 0, 550, 0, 500, 50,50)
clock =  time.Clock()
wal1 = Wall(0, 0, 0, 300, 300, 220, 15)
wal2 = Wall(0, 0, 0, 300, 150, 15, 320)
wal3 = Wall(0, 0, 0, 300, 150, 220, 15)
font.init()
font = font.Font(None,70)
win = font.render('Нас не догонят', True, (0,255,0))
lose = font.render('NIGGERS', True, (0,0,0))
Cat = font.render('Ой мама пришла', True, (255, 255, 255))
run = True
finish = False
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    if finish != True:
        window.blit(back, (0,0))
        # player.update()
        player.reset()
        player.move()
        wal1.reset()
        wal2.reset()
        wal3.reset()
        enemy.update()
        enemy.reset()
        final.reset()

        if sprite.collide_rect(player, final):
         finish = True
         window.blit(win, (150,250))

        if sprite.collide_rect(player, wal3) or sprite.collide_rect(player, wal1) or sprite.collide_rect(player, wal2):
            window.blit(lose, (350,250))
            finish = True

        if (sprite.collide_rect(player, enemy)):
                window.blit(Cat, (150,250))
                finish = True

    display.update()    
    clock.tick(60)

