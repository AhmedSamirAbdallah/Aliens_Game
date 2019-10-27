import pygame as p
from  settings import  Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group
from game_state import Game_Sate
from button import button
from scoreboard import scoreboard
def rungame():
    p.init()
    ai_Settings=Settings()
    screen=p.display.set_mode((ai_Settings.screen_width,ai_Settings.screen_heigth))
    ship=Ship(screen,ai_Settings)
    p.display.set_caption("Alien Invasion")
    play_button=button(ai_Settings,screen,"play")
    lose_button=button(ai_Settings,screen,"Gamal AbdelNaser")
    bullets=Group()
    aliens=Group()
    state=Game_Sate(ai_Settings)
    sb=scoreboard(screen,state,ai_Settings)
    gf.fleet_of_aliens(ai_Settings,screen,aliens,ship)
    while True:
        gf.check_event(state,play_button,ship,aliens,ai_Settings,screen,bullets,lose_button,sb)
        gf.update_screen(ai_Settings,screen,ship,bullets,aliens,state,play_button,lose_button,sb)
        if state.game_active:
            ship.update()
            bullets.update()
            gf.update_aliens(aliens,ai_Settings,ship,screen,bullets,state,sb)
            gf.update_bullets(bullets,aliens,ai_Settings,screen,ship,sb,state)
rungame()
