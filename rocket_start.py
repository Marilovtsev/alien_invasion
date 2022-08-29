import sys
import pygame

from rocket import Rocket
from rocket_set import Settings


class RocketStart:
    """Клас для керування ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру і створює игрові ресурси"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.rocket = Rocket(self.screen, self.settings)

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
        # При кожному проході циклу екран перемальовуєтся



if __name__ == '__main__':
    # Створення екземпляра та запуск гри.
    ai = RocketStart()
    ai.run_game()
