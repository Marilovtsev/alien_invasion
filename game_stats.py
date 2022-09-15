class GameStats():
    """Відстеження статистики для гри Alien Invasion"""

    def __init__(self, ai_game):
        """Ініціалізує статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
