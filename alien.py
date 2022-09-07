import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас, один прибулець."""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його початкову позицію."""
        super().__init__()
        self.screen = ai_game.screen

        # Завантаження зображення прибульця та призначення атрибуту rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється у лівому верхньому куті екрану.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Закріплення точної горизонтальної позиції прибульця.
        self.x = float(self.rect.x)
