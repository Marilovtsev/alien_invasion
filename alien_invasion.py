import sys
import pygame


class AlienInvasion:
    """Клас для керування ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру і створює игрові ресурси"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відстеження подій клавіатури та миші
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Відображення останнього промальованного екрану.
            pygame.display.flip()

if __name__ == '__main__':
    #Створення екземпляра та запуск гри.
    ai = AlienInvasion()
    ai.run_game()