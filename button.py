import pygame.font as pyf
import pygame
class button:
    def __init__(self,ai_Settings,screen,msg):
        self.screen=screen
        self.ai_Settings=ai_Settings
        self.button_color_rgb=(255, 239, 237)
        self.text_color_rgb=(255, 174, 237)
        self.screen_rect=screen.get_rect()
        self.shape=pyf.SysFont('Arial',45)
        self.rect=pygame.Rect(0,0,ai_Settings.button_width,ai_Settings.button_height)
        self.rect.centerx=self.screen_rect.centerx
        self.prep_msg(msg)
    def prep_msg(self,msg):
        self.msg_image=self.shape.render(msg,True,self.text_color_rgb,self.button_color_rgb)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.centerx=self.rect.centerx
    def draw_button(self):
        self.screen.fill(self.button_color_rgb,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
