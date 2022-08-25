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
        self.y = float(self.rect.y)

        # Флаг переміщення
        self.moving_right = False
        self.moving_left = False
        self.moving_height = False
        self.moving_width = False

    def update(self):
        """Оновлює позицію корабля з урахуванням флагів"""
        # Оновлює атрибут х, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_height and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.settings.rocket_speed
        if self.moving_width and self.rect.bottom < self.screen_rect.midbottom:
            self.rect.centery += self.settings.rocket_speed
        self.rect.centerx = self.center


        # Оновлення атрибуту rect на основі self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Малює корабель у нинішній позиції"""
        self.screen.blit(self.image, self.rect)
