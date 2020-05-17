class GameStats:
    """Track statistics for Alien Inavasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings

        # Try read high score and the high score in string format.
        filename = 'highscore.txt'

        with open(filename, 'r') as file_object:
            num = file_object.read()


        self.high_score = int(num)

        # High score should never be reset.

        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initilze stastics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
