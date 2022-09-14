import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас, один прибулець."""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його початкову позицію."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen = ai_game.settings

        # Завантаження зображення прибульця та призначення атрибуту rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється у лівому верхньому куті екрану.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Закріплення точної горизонтальної позиції прибульця.
        self.x = float(self.rect.x)

    def update(self):
        """Переміщує прибульця вправо"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
