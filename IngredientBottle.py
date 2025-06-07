import Ingredient
import pygame
from Constants import *

class IngredientBottle:
    def __init__(self, ingredient: Ingredient, x: int, y: int):
        self.ingredient = ingredient
        self.rect = pygame.Rect(x, y, 80, 120)
        self.is_pouring = False
        self.font = pygame.font.Font(None, 20)
        self.pour_rate = 0.008  # Ilość nalewana za frame podczas trzymania
        self.mouse_held = False

    def draw(self, screen, ingredient_images):
        image = ingredient_images.get(self.ingredient.name)

        if image:
            # Rysuj obrazek jako butelkę
            image_rect = image.get_rect(center=self.rect.center)
            screen.blit(image, image_rect)
            self.rect = image_rect  # aktualizacja kolizji do rozmiaru obrazka
        else:
            # Fallback jeśli brak obrazka
            pygame.draw.rect(screen, self.ingredient.color, self.rect)
            pygame.draw.rect(screen, BLACK, self.rect, 2)

        # Nazwa pod butelką
        name_surface = self.font.render(self.ingredient.name[:8], True, BLACK)
        name_rect = name_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 15))
        screen.blit(name_surface, name_rect)

    def handle_event(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.mouse_held = True
                self.is_pouring = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_held = False
                self.is_pouring = False

        # Sprawdź czy mysz nadal jest nad butelką podczas trzymania
        if self.mouse_held:
            if not self.rect.collidepoint(mouse_pos):
                self.is_pouring = False
            else:
                self.is_pouring = True
                return True

        return False