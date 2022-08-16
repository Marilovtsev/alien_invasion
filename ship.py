import pygame

class Ship():
    """Скласс для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та задає його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажує зображення корабля та отримує прямокутник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Кожен новий корабель з'ялвяється у нижньому куті екрану
        self.rect.midbottom = self.screen_rect.midbottom