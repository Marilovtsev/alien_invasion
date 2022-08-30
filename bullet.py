import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing bullets fired by a ship."""

    def __init__(self, ai_game):
        """Creates a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
