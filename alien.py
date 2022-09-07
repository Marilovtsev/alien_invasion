import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас, один прибулець."""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його початкову позицію."""
        super().__init__()
        self.screen = ai_game.screen
