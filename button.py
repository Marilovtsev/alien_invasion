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

        # Будування об'єкту rect кнопки та вирівнювання по центру екрану
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Повідомлення кнопки створюється тільки один раз
        self.prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворює msg в прямокутник та вирівнює текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
