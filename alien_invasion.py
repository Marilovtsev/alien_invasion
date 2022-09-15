import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Клас для керування ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру і створює игрові ресурси"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        # Створення екземпляру для зберігання ігрової статистики.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()

            # print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        """Обробляє натискання клавіатури та події миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагує на натискання клавіш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагує на відпускання клавіш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and include it in the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Оновлює позиції снарядів та знищує старі снаряди"""
        # Updated projectile positions.
        self.bullets.update()

        # Removing projectiles that have gone off the edge of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обробка колізій снарядів з прибульцями"""
        # Видалення снарядів та прибульців у колізії
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens,
                                                True, True)

        if not self.aliens:
            # Знищення існуючих снарядів та створення нового флоту
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Оновлює позиції усіх прибульців у флоті"""
        self._check_fleet_edges()
        self.aliens.update()

        # Перевірка колізій "прибулець - корабель"
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship hit!!!')

    def _ship_hit(self):
        """Обробляємозіткнення коробля з прибульцем."""
        # Зменшення ship_left.
        self.stats.ships_left -= 1



    def _create_fleet(self):
        """Створення флоту вторгнення"""
        # створення прибульця та вирахування кількості прибульців в ряді
        # нтервал муж сусідніми прибульцями дорівнює ширині прибульця
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Визначає кількість рядів, що помістяться на екрані"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Створення флоту вторгення.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Створення прибульця та розміщення його у ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """реагує на досягнення прибульцем краю екрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускає увесь флот та міняє напрямок"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Оновлює зображення на екрані та відображає новий екран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def change_fleet_direction(self):
        pass


if __name__ == '__main__':
    # Створення екземпляра та запуск гри.
    ai = AlienInvasion()
    ai.run_game()
