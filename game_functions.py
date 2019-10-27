import pygame as p
import sys
from bullet import Bullet
from Alien import Alines
from pygame.sprite import groupcollide
from pygame.sprite import spritecollideany
import time
def check_event(state,play_button,ship,aliens,ai_Settings,screen,bullets,lose_button,sb):
    for event in p.event.get():
        if event.type==p.QUIT:
            sys.exit()
        elif event.type==p.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=p.mouse.get_pos()
            check_play_button(state,play_button,mouse_x,mouse_y,ship,aliens,ai_Settings,screen,bullets,sb)
        elif event.type==p.KEYDOWN:
            check_KEYDOWN(event,ai_Settings,ship,screen,bullets)
        elif event.type==p.KEYUP:
            check_KEYUP(ship,event)
def update_screen(ai_Settings,screen,ship,bullets,aliens ,state,play_button,lose_button,sb):
    screen.fill(ai_Settings.b_g)
    ship.blmit()
    sb.show_score()
    for bul in bullets.sprites():
        bul.draw_bullet()
    aliens.draw(screen)
    if not state.game_active and state.ship_left<=0:
        lose_button.draw_button()
    elif not state.game_active:
        play_button.draw_button()
    p.display.flip()
def check_KEYDOWN(event,ai_Settings,ship,screen,bullets):
    if event.key==p.K_ESCAPE:
        sys.exit()
    elif event.key==p.K_RIGHT:
        ship.moving_right=True
    elif event.key==p.K_LEFT:
        ship.moving_left=True
    elif event.key==p.K_SPACE:
        fire_bullet(bullets,ai_Settings,ship,screen)
def check_KEYUP(ship,event):
    if event.key==p.K_RIGHT:
        ship.moving_right=False
    elif event.key==p.K_LEFT:
        ship.moving_left=False
def get_rid_of_bullets(bullets):
    for bul in bullets:
        if bul.rect.bottom<=0:
            bullets.remove(bul)
def check_bullet_alien_collisions(ai_Settings,screen,aliens,ship,bullets,sb,state):
    collisions=groupcollide(bullets ,aliens,True,True)
    if collisions:
        for alien in collisions.values():
            state.score+=ai_Settings.alien_point*(len(alien))
            sb.pre_score()
        check_high_score(state,sb)
    if len(aliens)==0:
        bullets.empty()
        ai_Settings.increse_speed()
        state.level+=1
        sb.pre_level()
        fleet_of_aliens(ai_Settings,screen,aliens,ship)
def update_bullets(bullets,aliens,ai_Settings,screen,ship,sb,state):
    get_rid_of_bullets(bullets)
    check_bullet_alien_collisions(ai_Settings,screen,aliens,ship,bullets,sb,state)
def check_ship_alien_collisions(ship,aliens,ai_Settings,screen,bullets,state,sb):
    if spritecollideany(ship,aliens):
        ship_hit(ship,aliens,ai_Settings,screen,bullets,state,sb)
def fire_bullet(bullets,ai_Settings,ship,screen):
    if len(bullets)<ai_Settings.allowed_bullets:
        new_bullet=Bullet(ai_Settings,ship,screen)
        bullets.add(new_bullet)
def fleet_of_aliens(ai_Settings,screen,aliens,ship):
    num_aliens=get_number_of_alines(ai_Settings)
    num_row=get_num_of_rows(ai_Settings,screen,)
    create_alien(ai_Settings,screen,num_aliens,aliens,num_row,ship)
def create_alien(ai_Settings,screen,num_aliens,aliens,num_row,ship):
    for num_of_rows in range(num_row):
        for num_of_aliens in range(num_aliens):
            instance=Alines(screen,ai_Settings,ship)
            instance.x=ai_Settings.aliens_width+(2*ai_Settings.aliens_width)*num_of_aliens
            instance.y=(2*ai_Settings.aliens_hight)*num_of_rows
            instance.rect.x=instance.x
            instance.rect.y=instance.y
            aliens.add(instance)
def get_num_of_rows(ai_Settings,screen):
    space_height=ai_Settings.screen_heigth-ai_Settings.aliens_hight-ai_Settings.ship_height
    number_of_rows=int(space_height/(2*ai_Settings.aliens_hight))
    return int(number_of_rows/2)
def get_number_of_alines(ai_Settings):
    space_available=ai_Settings.screen_width-2*ai_Settings.aliens_width
    number_of_aliens=int(space_available/(2*ai_Settings.aliens_width))
    return number_of_aliens
def update_aliens(aliens,ai_Settings,ship,screen,bullets,state,sb):
    check_fleet_edges(ai_Settings,aliens)
    aliens.update()
    check_ship_alien_collisions(ship,aliens,ai_Settings,screen,bullets,state,sb)
    aliens_reach_bottom(ship,aliens,ai_Settings,screen,bullets,state,sb)
def check_fleet_edges(ai_Settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_Settings,aliens)
            break
def change_fleet_direction(ai_Settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_Settings.fleet_drop_speed
    ai_Settings.direction*=-1
    print(ai_Settings.direction)
def ship_hit(ship,aliens,ai_Settings,screen,bullets,state,sb):
    state.ship_left -=1
    if state.ship_left >0:
        state.game_active=True
        sb.try_hard()
        aliens.empty()
        bullets.empty()
        time.sleep(2)
        ship.recenter_the_ship()
        fleet_of_aliens(ai_Settings,screen,aliens,ship)
    else:
        state.game_active=False
        p.mouse.set_visible(True)
def aliens_reach_bottom(ship,aliens,ai_Settings,screen,bullets,state,sb):
    screen_rect=screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom>screen_rect.bottom :
            ship_hit(ship,aliens,ai_Settings,screen,bullets,state,sb)
            break
def check_play_button(state,play_button,mouse_x,mouse_y,ship,aliens,ai_Settings,screen,bullets,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not state.game_active:
        ai_Settings.init_dynamic()
        p.mouse.set_visible(False)
        state.rest_game()
        state.game_active=True
        sb.pre_score()
        sb.pre_high_score()
        sb.pre_level()
        sb.try_hard()
        aliens.empty()
        bullets.empty()
        fleet_of_aliens(ai_Settings,screen,aliens,ship)
        ship.recenter_the_ship()
def check_high_score(state,sb):
    if state.score>state.high_score:
        state.high_score=state.score
        sb.pre_high_score()
