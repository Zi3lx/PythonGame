from Constants import *
import pygame
import random
from typing import List, Dict, Optional, Tuple

class Shaker:
    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, 120, 180)
        self.contents: Dict[str, float] = {}
        self.font = pygame.font.Font(None, 24)
        self.is_shaking = False
        self.shake_animation = 0
        self.max_capacity = 1.0
        self.is_mixed = False  # Czy drink został wymieszany
        self.mixing_quality = 1.0  # Jakość mieszania (0.5-1.0)
        self.overshaken = False  # Czy został za bardzo wstrząśnięty
        self.shake_count = 0  # Ilość wstrząśnięć

    def add_ingredient(self, ingredient_name: str, amount: float = 0.008):
        current_total = sum(self.contents.values())

        if current_total >= self.max_capacity:
            return False  # Shaker pełny

        available_space = self.max_capacity - current_total
        actual_amount = min(amount, available_space)

        if ingredient_name not in self.contents:
            self.contents[ingredient_name] = 0

        self.contents[ingredient_name] += actual_amount

        # Dodanie składnika psuje mieszanie
        self.is_mixed = False
        return True

    def clear(self):
        self.contents.clear()
        self.is_shaking = False
        self.is_mixed = False
        self.mixing_quality = 1.0
        self.overshaken = False
        self.shake_count = 0

    def shake(self):
        if not self.contents:
            return False

        self.is_shaking = True
        self.shake_animation = 60  # Dłuższa animacja
        self.shake_count += 1

        # Logika mieszania
        if self.shake_count == 1:
            # Pierwsze wstrząśnięcie - dobre mieszanie
            self.is_mixed = True
            self.mixing_quality = 1.0
        elif self.shake_count == 2:
            # Drugie wstrząśnięcie - nadal ok
            self.mixing_quality = 0.95
        elif self.shake_count == 3:
            # Trzecie - lekko za dużo
            self.mixing_quality = 0.85
            self.overshaken = True
        else:
            # Za dużo wstrząśnięć - psucie drinku
            self.mixing_quality = max(0.5, self.mixing_quality - 0.1)
            self.overshaken = True

        return True

    def update(self):
        if self.shake_animation > 0:
            self.shake_animation -= 1
        if self.shake_animation == 0:
            self.is_shaking = False

    def get_normalized_contents(self):
        """Zwraca zawartość jako proporcje (suma = 1.0)"""
        total = sum(self.contents.values())
        if total == 0:
            return {}

        return {ingredient: amount / total for ingredient, amount in self.contents.items()}

    def get_mixing_penalty(self):
        """Zwraca karę za złe mieszanie"""
        if not self.contents:
            return 1.0

        if not self.is_mixed:
            return 0.3  # Nie wymieszane = duża kara

        return self.mixing_quality

    def draw(self, screen):
        # Shaker z animacją trzęsienia
        shake_intensity = 5 if self.is_shaking else 0
        offset_x = random.randint(-shake_intensity, shake_intensity)
        offset_y = random.randint(-shake_intensity, shake_intensity)

        shaker_rect = pygame.Rect(self.rect.x + offset_x, self.rect.y + offset_y,
                                  self.rect.width, self.rect.height)

        pygame.draw.rect(screen, LIGHT_GRAY, shaker_rect)
        pygame.draw.rect(screen, BLACK, shaker_rect, 3)

        # Wyświetlanie zawartości jako warstwy
        total_amount = sum(self.contents.values())
        if total_amount > 0:
            y_offset = 0
            max_height = shaker_rect.height - 40

            # Efekt mieszania - jeśli nie wymieszane, składniki są rozdzielone
            if self.is_mixed:
                # Wymieszane - jedna warstwa mieszanego koloru
                mixed_color = self._get_mixed_color()
                layer_height = int((total_amount / self.max_capacity) * max_height)
                if layer_height > 0:
                    content_rect = pygame.Rect(
                        shaker_rect.x + 10,
                        shaker_rect.bottom - 20 - layer_height,
                        shaker_rect.width - 20,
                        layer_height
                    )
                    pygame.draw.rect(screen, mixed_color, content_rect)
            else:
                # Nie wymieszane - osobne warstwy
                for ingredient, amount in self.contents.items():
                    if amount > 0:
                        layer_height = int((amount / self.max_capacity) * max_height)
                        if layer_height > 0:
                            content_rect = pygame.Rect(
                                shaker_rect.x + 10,
                                shaker_rect.bottom - 20 - y_offset - layer_height,
                                shaker_rect.width - 20,
                                layer_height
                            )
                            color = self._get_ingredient_color(ingredient)
                            pygame.draw.rect(screen, color, content_rect)
                            y_offset += layer_height

        # Status mieszania
        if self.contents:
            if not self.is_mixed:
                status_text = self.font.render("NIEWYM.", True, RED)
                screen.blit(status_text, (shaker_rect.x - 60, shaker_rect.y))
            elif self.overshaken:
                status_text = self.font.render("PRZEM.", True, ORANGE)
                screen.blit(status_text, (shaker_rect.x - 60, shaker_rect.y))
            else:
                status_text = self.font.render("OK", True, GREEN)
                screen.blit(status_text, (shaker_rect.x - 30, shaker_rect.y))

        # Pasek pojemności
        capacity_rect = pygame.Rect(shaker_rect.right + 10, shaker_rect.y, 20, shaker_rect.height)
        pygame.draw.rect(screen, WHITE, capacity_rect)
        pygame.draw.rect(screen, BLACK, capacity_rect, 2)

        if total_amount > 0:
            fill_height = int((total_amount / self.max_capacity) * capacity_rect.height)
            fill_rect = pygame.Rect(capacity_rect.x, capacity_rect.bottom - fill_height,
                                    capacity_rect.width, fill_height)
            color = GREEN if total_amount < 0.9 else RED
            pygame.draw.rect(screen, color, fill_rect)

    def _get_mixed_color(self):
        """Zwraca kolor wymieszanych składników"""
        if not self.contents:
            return WHITE

        total_r = total_g = total_b = 0
        total_amount = 0

        color_map = {
            "Wódka": WHITE,
            "Rum": BROWN,
            "Whiskey": ORANGE,
            "Gin": WHITE,
            "Sok pomarańczowy": ORANGE,
            "Sok żurawinowy": RED,
            "Lemoniada": YELLOW,
            "Cola": BLACK,
            "Grenadina": RED,
            "Wermut": DARK_GREEN,
            "Sprite": WHITE,
            "Sok ananasowy": YELLOW
        }

        for ingredient, amount in self.contents.items():
            if amount > 0 and ingredient in color_map:
                color = color_map[ingredient]
                total_r += color[0] * amount
                total_g += color[1] * amount
                total_b += color[2] * amount
                total_amount += amount

        if total_amount > 0:
            return (int(total_r / total_amount),
                    int(total_g / total_amount),
                    int(total_b / total_amount))
        return WHITE

    def _get_ingredient_color(self, ingredient_name):
        color_map = {
            "Wódka": WHITE,
            "Rum": BROWN,
            "Whiskey": ORANGE,
            "Gin": WHITE,
            "Sok pomarańczowy": ORANGE,
            "Sok żurawinowy": RED,
            "Lemoniada": YELLOW,
            "Cola": BLACK,
            "Grenadina": RED,
            "Wermut": DARK_GREEN,
            "Sprite": WHITE,
            "Sok ananasowy": YELLOW
        }
        return color_map.get(ingredient_name, GRAY)

