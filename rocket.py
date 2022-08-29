import pygame


class Rocket:
    """Класс для керування кораблем"""

    def __init__(self, settings, screen):
        """Ініціалізує корабель та задає його початкову позицію"""
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/spacecraft-g5e4182639_640.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.image.set_colorkey((255, 255, 255))

    def update(self):
        """Оновлює позицію корабля з урахуванням флагів"""
        # Оновлює атрибут х, не rect
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.rocket_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.rocket_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        # # Оновлення атрибуту rect на основі self.x
        # self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        """Малює корабель у нинішній позиції"""
        self.screen.blit(self.image, self.rect)
