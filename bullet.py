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

        # Creating a bullet at position (0,0) and assigning the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.screen_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The position of the bullet is stored in real format.
        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet up the screen."""
        # Bullet position update in real format
        self.y -= self.settings.bullet_speed

        # Update the position of the rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Output the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
