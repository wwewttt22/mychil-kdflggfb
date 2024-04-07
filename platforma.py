from pygame import *
from gamesprite import GameSprite

class Platform(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y + self.rect.height < 620:
            self.rect.y += self.speed

    def update_right(self):
        keys2 = key.get_pressed()
        if keys2[K_UP] and self.rect.y > -20:
            self.rect.y -= self.speed
        if keys2[K_DOWN] and self.rect.y + self.rect.height < 620:
            self.rect.y += self.speed

    def reset(self):
        self.window.blit(self.img, (self.rect.x, self.rect.y))