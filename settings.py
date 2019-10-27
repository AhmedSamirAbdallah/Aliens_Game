class  Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_heigth=800
        self.b_g=(255,255,255)
        self.ship_speed_factor=2
        self.bullet_width=10
        self.bullet_hight=5
        self.bullet_speed_factor=2
        self.bullet_color=(60,60,60)
        self.allowed_bullets=3
        self.aliens_width=70
        self.aliens_hight=30
        self.alien_speed_factor=1
        self.direction=1
        self.fleet_drop_speed=10
        self.ship_width=200
        self.ship_height=100
        self.ship_limits=3
        self.button_width=150
        self.button_height=70
        self.speed_scale=1.1
        self.score_scale=1.5
        self.init_dynamic()
    def init_dynamic(self):
           self.bullet_speed_factor=2
           self.ship_speed_factor=2
           self.alien_speed_factor=1
           self.direction=1
           self.alien_point=50
    def increse_speed(self):
        self.bullet_speed_factor*=self.speed_scale
        self.ship_speed_factor*=self.speed_scale
        self.alien_speed_factor*=self.speed_scale
        self.alien_point=int(self.alien_point*self.score_scale)
