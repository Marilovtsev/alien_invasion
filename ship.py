import pygame

class Ship():
    """Скласс для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та задає його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()