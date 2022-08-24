import pygame


class Rocket():
    """Класс для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та задає його початкову позицію"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажує зображення корабля та отримує прямокутник
        self.image = pygame.image.load('images/spacecraft-g5e4182639_640.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        # Кожен новий корабель з'ялвяється у нижньому куті екрану
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберігання речової координати центру корабля
        self.x = float(self.rect.x)

        # Флаг переміщення
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Оновлює позицію корабля з урахуванням флагів"""
        # Оновлює атрибут х, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Оновлення атрибуту rect на основі self.x
        self.rect.x = self.x

    def blitme(self):
        """Малює корабель у нинішній позиції"""
        self.screen.blit(self.image, self.rect)
