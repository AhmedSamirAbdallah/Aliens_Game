class Game_Sate:
    def __init__(self,ai_Settings):
        self.game_active=False
        self.ai_Settings=ai_Settings
        self.high_score=0
        self.rest_game()
    def rest_game(self):
        self.ship_left=self.ai_Settings.ship_limits
        self.score=0
        self.level=1
