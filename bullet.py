import pygame as p
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_Settings,ship,screen):
        super().__init__()
        self.screen=screen
        self.rect=p.Rect(0,0,ai_Settings.bullet_width,ai_Settings.bullet_hight)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=ai_Settings.bullet_color
        self.speed_factor=ai_Settings.bullet_speed_factor
    def update(self):
        self.rect.y=self.y
        self.y-=self.speed_factor
    def draw_bullet(self):
        p.draw.rect(self.screen,self.color,self.rect)
