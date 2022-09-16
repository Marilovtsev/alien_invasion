class Settings():
    """Класс для зберігання усіх налаштувань гри Alien Invasion"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Monitor settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 30, 80)
        self.bullet_allowed = 3
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet direction = 1 означає рух вправо; f -1 - вліво
        self.fleet_direction = 1
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet parameters
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (50, 50, 150)
