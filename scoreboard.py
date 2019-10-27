import pygame.font
class scoreboard:
    def __init__(self,screen,state,ai_Settings):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.state=state
        self.ai_Settings=ai_Settings
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.pre_score()
        self.pre_high_score()
        self.pre_level()
        self.try_hard()
    def pre_score(self):
            rounded_score=round(self.state.score,-1)
            str_score=str(format(rounded_score,','))
            self.img_score=self.font.render(str_score,True,self.text_color,self.ai_Settings.b_g)
            self.score_rect=self.img_score.get_rect()
            self.score_rect.right=self.screen_rect.right-20
            self.score_rect.top=20
    def pre_high_score(self):
        high_score=round(self.state.high_score,-1)
        str_high_score=str(format(high_score,','))
        self.high_score_image=self.font.render(str_high_score,True,self.text_color,self.ai_Settings.b_g)
        self.rect_high_score=self.high_score_image.get_rect()
        self.rect_high_score.centerx=self.screen_rect.centerx
        self.rect_high_score.top=self.screen_rect.top
    def pre_level(self):
        self.level_img=self.font.render(str(self.state.level),True,self.text_color,self.ai_Settings.b_g)
        self.rect_level=self.level_img.get_rect()
        self.rect_level.right=self.screen_rect.right-20
        self.rect_level.top=self.score_rect.bottom+10
    def try_hard(self):
            self.tries=self.font.render(("TRY: "+str(self.state.ship_left)),True,self.text_color,self.ai_Settings.b_g)
            self.rect_try=self.tries.get_rect()
            self.rect_try.left=self.screen_rect.left
            self.rect_try.top=self.screen_rect.top
    def show_score(self):
        self.screen.blit(self.img_score,self.score_rect)
        self.screen.blit(self.high_score_image,self.rect_high_score)
        self.screen.blit(self.level_img,self.rect_level)
        self.screen.blit(self.tries,self.rect_try)
