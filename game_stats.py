class GameStats:
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initialize statistics"""
        # high score should never reset 
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()

        #Start alien invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        # Add more statistics as needed, such as score, level, etc.

        #scoring 
        self.score = 0 
        self.level = 1

