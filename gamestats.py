class GameStats():
    """追踪游戏的统计信息"""
    def __init__(self,ship_settings):
        """初始化统计信息"""
        
        self.game_active =False
        self.ship_settings = ship_settings

        
        self.high_score = 0

        self.reset_stats()
        
        


    def reset_stats(self):
        
        self.ships_left = self.ship_settings.limit
       
        self.score = 0
        
        self.sun_number = 50
      
        self.level = 1
   
        self.trick = 1
        self.trick_flag = True
     
        self.ship = "Peashooter"

    def check_high_score(self):
        
        if self.score > self.high_score :
            self.high_score = self.score

    def check_level(self):

        if self.score >= 5000 and self.score <15000:
            self.level = 2
        elif self.score >= 15000 and self.score <30000:
            self.level = 3
        elif self.score >= 30000 and self.score <50000:
            self.level = 4
        elif self.score >= 50000 and self.score <750000:
            self.level = 5

