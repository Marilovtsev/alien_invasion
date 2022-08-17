import pygame


class Ship():
    """Класс для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та задає його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажує зображення корабля та отримує прямокутник
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # Кожен новий корабель з'ялвяється у нижньому куті екрану
        self.rect.midbottom = self.screen_rect.midbottom

        #Флаг переміщення
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Оновлює позицію корабля з урахуванням флагів"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x += 1

    def blitme(self):
        """Малює корабель у нинішній позиції"""
        self.screen.blit(self.image, self.rect)
