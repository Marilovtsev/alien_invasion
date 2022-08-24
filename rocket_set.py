class Settings():
    """Класс для зберігання усіх налаштувань гри Alien Invasion"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Monitor settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 200, 250)

        # Ship settings
        self.ship_speed = 1.5