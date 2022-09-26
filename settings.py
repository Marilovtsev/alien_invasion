class Settings():
    """Класс для зберігання усіх налаштувань гри Alien Invasion"""

    def __init__(self):
        """Ініціалізує статистичні налаштування гри"""
        # Monitor settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 30, 80)
        self.bullet_allowed = 3
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10

        # fleet direction = 1 означає рух вправо; f -1 - вліво
        self.fleet_direction = 1
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2

        # Bullet parameters
        self.bullet_speed = 1
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color = (50, 50, 150)

        # Темп прискорення гри
        self.speedup_scale = 5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізує налаштування, які змінюються під час гри."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 означає рух вправо, а -1 - вліво.
        self.fleet_direction = 1

    def increase_speed(self):
        """Збільшує налатшування швидкості."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
