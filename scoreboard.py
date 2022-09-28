import pygame.font


class Scoreboard():
    """Класс для виводу ігрової інформації"""

    def __init__(self, ai_game):
        """Ініціалізує атрибути підрахунку поінтів"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифту для вивода рахунку
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)
        # Підготовка зображення рахунків
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Преобразує нинішній рахунок у графічне зображення"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # Вивід рахунку у правій частині екрану.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразує рекордний рахунок у графічне зображення"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.ai_settings.bg_color)


    def show_score(self):
        """Виводить рахунок на екран"""
        self.screen.blit(self.score_image, self.score_rect)
