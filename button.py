import pygame.font


class Button():

    def __init__(self, ai_game, msg):
        """Ініціалізує атрибути кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Встановлення розміру та властивостей кнопок.
        self.width, self.height = 200, 50  # СКОРІШ ЗА ВСЕ ПОТРІБНІ ДУЖКИ
        self.button_color = (0, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

