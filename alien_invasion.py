import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Клас для керування ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру і створює игрові ресурси"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            self._check_events()
        #При кожному проході циклу екран перемальовуєтся

    def _check_events(self):
            """Відстеження подій клавіатури та миші"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При кожному проході циклу екран перемальовуєтся
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Відображення останнього промальованного екрану.
            pygame.display.flip()


if __name__ == '__main__':
    # Створення екземпляра та запуск гри.
    ai = AlienInvasion()
    ai.run_game()
