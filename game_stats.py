class GameStats():
    """Відстеження статистики для гри Alien Invasion"""

    def __init__(self, ai_game):
        """Ініціалізує статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Ініціалізує статистику, яка змінюється під час гри."""
        self.ships_left = self.settings.ship_limit
