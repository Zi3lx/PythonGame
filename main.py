import pygame
import json
import random
import math
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from Constants import *
from IngredientBottle import IngredientBottle
from Ingredient import Ingredient
from Button import Button
from Shaker import Shaker
from DrinkRecipe import DrinkRecipe
from Matcher import DrinkMatcher
from PlayerName import *
from DrinksDB import *

# Inicjalizacja Pygame
pygame.init()

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    RESULT = 3
    PAUSE = 4
    NAME_INPUT = 5

class BartenderGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("POLEJ MI")
        self.clock = pygame.time.Clock()

        self.state = GameState.MENU
        self.score = 0
        self.drinks_made = 0
        self.last_result = None
        self.player_name = ""
        self.name_input = PlayerNameInput(SCREEN_WIDTH // 2 - 100, 250, 200, 40)
        self.asking_for_name = True

        # Inicjalizacja składników
        self.ingredients = get_ingredients()

        # Baza drinków
        self.drink_database = get_drink_recipes()

        self.drink_matcher = DrinkMatcher(self.drink_database)

        # Elementy UI
        self.ingredient_bottles = []
        for i, ingredient in enumerate(self.ingredients):
            x = 50 + (i % 6) * 95
            y = 150 + (i // 6) * 210
            self.ingredient_bottles.append(IngredientBottle(ingredient, x, y))

        self.ingredient_images = {}
        for ingredient in self.ingredients:
            if ingredient.image_path:
                try:
                    image = pygame.image.load(ingredient.image_path)
                    image = pygame.transform.scale(image, (80, 120))
                    self.ingredient_images[ingredient.name] = image
                except:
                    print(f"Nie udało się załadować obrazu dla: {ingredient.name}")

        self.shaker = Shaker(750, 450)

        # Przyciski
        self.shake_button = Button(750, 640, 100, 40, "SHAKE", GREEN)
        self.serve_button = Button(860, 640, 100, 40, "SERVE", BLUE)
        self.clear_button = Button(750, 690, 100, 40, "CLEAR", RED)
        self.menu_button = Button(860, 690 , 100, 40, "MENU", GRAY)
        self.continue_button = Button(750, 590, 210, 40, "NEXT DRINK", GREEN)

        # Menu buttons
        self.start_button = Button(SCREEN_WIDTH // 2 - 100, 300, 200, 50, "START GAME", GREEN)
        self.quit_button = Button(SCREEN_WIDTH // 2 - 100, 370, 200, 50, "QUIT", RED)

        self.confirm_name_button = Button(SCREEN_WIDTH // 2 - 100, 320, 200, 40, "POTWIERDŹ", GREEN)

        # Fonty
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.font_tiny = pygame.font.Font(None, 18)

        self.high_scores = self.load_scores()

    def load_scores(self):
        try:
            with open('bartender_scores.json', 'r') as f:
                scores = json.load(f)
                # Kompatybilność z starym formatem
                if scores and isinstance(scores[0], int):
                    return [{"name": "Anonim", "score": score, "drinks": 0} for score in scores]
                return scores
        except FileNotFoundError:
            return []

    def save_scores(self):
        # Dodaj nowy wynik w formacie słownika
        new_score = {
            "name": self.player_name if self.player_name else "Anonim",
            "score": self.score,
            "drinks": self.drinks_made
        }
        self.high_scores.append(new_score)

        # Upewnij się, że wszystkie wyniki są w formacie słownika
        normalized_scores = []
        for score_entry in self.high_scores:
            if isinstance(score_entry, dict):
                normalized_scores.append(score_entry)
            else:  # stary format - tylko liczba
                normalized_scores.append({
                    "name": "Anonim",
                    "score": score_entry,
                    "drinks": 0
                })

        # Sortuj według punktów (score)
        normalized_scores.sort(key=lambda x: x["score"], reverse=True)

        # Zachowaj tylko 10 najlepszych
        self.high_scores = normalized_scores[:10]

        try:
            with open('bartender_scores.json', 'w') as f:
                json.dump(self.high_scores, f)
        except:
            pass

    def serve_drink(self):
        normalized_drink = self.shaker.get_normalized_contents()

        if not normalized_drink:
            self.last_result = {
                'match': None,
                'similarity': 0.0,
                'points': 0,
                'message': "Shaker jest pusty!",
                'mixing_bonus': 1.0
            }
            return

        best_match, similarity, base_points = self.drink_matcher.find_best_match(normalized_drink)

        # Modyfikator za mieszanie
        mixing_bonus = self.shaker.get_mixing_penalty()
        final_points = int(base_points * mixing_bonus)

        self.score += final_points
        self.drinks_made += 1

        if not self.shaker.is_mixed:
            message = "Nie wymieszane! "
        elif self.shaker.overshaken:
            message = "Przemieszone! "
        else:
            message = ""

        if similarity >= 0.95:
            message += "PERFEKCYJNY!"
        elif similarity >= 0.8:
            message += "Wspaniały drink!"
        elif similarity >= 0.6:
            message += "Dobry drink!"
        elif similarity >= 0.4:
            message += "Niezły, ale można lepiej"
        elif similarity >= 0.2:
            message += "Słaby drink..."
        else:
            message += "Co to jest?!"

        self.last_result = {
            'match': best_match,
            'similarity': similarity,
            'points': final_points,
            'base_points': base_points,
            'message': message,
            'player_drink': normalized_drink.copy(),
            'mixing_bonus': mixing_bonus,
            'shake_count': self.shaker.shake_count,
            'was_mixed': self.shaker.is_mixed
        }

        self.state = GameState.RESULT

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if self.asking_for_name:
                # Obsługa wpisywania imienia
                if self.name_input.handle_event(event):
                    self.player_name = self.name_input.text.strip() or "Anonim"
                    self.asking_for_name = False
                    return True

                if self.confirm_name_button.handle_event(event):
                    self.player_name = self.name_input.text.strip() or "Anonim"
                    self.asking_for_name = False
                    return True

            if self.state == GameState.MENU:
                if self.start_button.handle_event(event):
                    self.state = GameState.PLAYING
                    self.score = 0
                    self.drinks_made = 0
                    self.shaker.clear()
                elif self.quit_button.handle_event(event):
                    return False

            elif self.state == GameState.PLAYING:
                mouse_pos = pygame.mouse.get_pos()

                # Obsługa butelek - ciągłe nalewanie
                for bottle in self.ingredient_bottles:
                    if bottle.handle_event(event, mouse_pos):
                        if bottle.is_pouring:
                            success = self.shaker.add_ingredient(bottle.ingredient.name, bottle.pour_rate)
                            if not success:
                                pass

                # Obsługa przycisków
                if self.shake_button.handle_event(event):
                    if not self.shaker.shake():
                        # Nie można wstrząsnąć pustego shakera
                        pass

                elif self.serve_button.handle_event(event):
                    self.serve_drink()

                elif self.clear_button.handle_event(event):
                    self.shaker.clear()

                elif self.menu_button.handle_event(event):
                    self.save_scores()
                    self.state = GameState.MENU

            elif self.state == GameState.RESULT:
                if self.continue_button.handle_event(event):
                    self.shaker.clear()
                    self.state = GameState.PLAYING
                elif self.menu_button.handle_event(event):
                    self.save_scores()
                    self.state = GameState.MENU

        return True

    def update(self):
        if self.state == GameState.PLAYING:
            self.shaker.update()

            # Ciągłe nalewanie podczas trzymania myszy
            mouse_pos = pygame.mouse.get_pos()
            for bottle in self.ingredient_bottles:
                if bottle.is_pouring:
                    success = self.shaker.add_ingredient(bottle.ingredient.name, bottle.pour_rate)
                    if not success:
                        # Shaker pełny
                        pass
        if self.asking_for_name:
            self.name_input.update()

    def draw_menu(self):
        self.screen.fill(WHITE)

        # Tytuł
        title_text = self.font_large.render("POLEJ MI", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)

        if self.asking_for_name:
            # Ekran wpisywania nazwy
            name_text = self.font_medium.render("Podaj swoje imię:", True, BLACK)
            name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
            self.screen.blit(name_text, name_rect)

            self.name_input.draw(self.screen)

            hint_text = self.font_small.render("Naciśnij Enter lub przycisk aby kontynuować", True, GRAY)
            hint_rect = hint_text.get_rect(center=(SCREEN_WIDTH // 2, 380))
            self.screen.blit(hint_text, hint_rect)

            # Przycisk potwierdzenia
            self.confirm_name_button.draw(self.screen)
        else:
            # Powitanie gracza
            if self.player_name:
                welcome_text = self.font_medium.render(f"Witaj, {self.player_name}!", True, BLUE)
                welcome_rect = welcome_text.get_rect(center=(SCREEN_WIDTH // 2, 130))
                self.screen.blit(welcome_text, welcome_rect)

            # Opis
            desc_lines = [
                "Mieszaj drinki bez przepisów!",
                "Gra zgadnie co stworzyłeś i przyzna punkty",
                "za podobieństwo do prawdziwych koktajli.",
                "",
                "WAŻNE: Pamiętaj o wstrząśnięciu shakera!"
            ]

            start_y = 160 if self.player_name else 150
            for i, line in enumerate(desc_lines):
                desc_text = self.font_small.render(line, True, BLACK)
                desc_rect = desc_text.get_rect(center=(SCREEN_WIDTH // 2, start_y + i * 25))
                self.screen.blit(desc_text, desc_rect)

            # Najlepsze wyniki
            scores_y = start_y + len(desc_lines) * 25 + 20
            scores_text = self.font_medium.render("Najlepsze wyniki:", True, BLACK)
            self.screen.blit(scores_text, (50, scores_y))

            for i, score_data in enumerate(self.high_scores[:5]):
                if isinstance(score_data, dict):
                    score_text = self.font_small.render(f"{i + 1}. {score_data['name']}: {score_data['score']} pkt",
                                                        True, BLACK)
                else:
                    score_text = self.font_small.render(f"{i + 1}. Anonim: {score_data} pkt", True, BLACK)
                self.screen.blit(score_text, (50, scores_y + 30 + i * 25))

            # Przyciski menu
            self.start_button.draw(self.screen)
            self.quit_button.draw(self.screen)

    def draw_game(self):
        background_img = pygame.image.load("assets/bar.png")
        background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(background_img, (0, 0))

        # Informacje o grze
        score_text = self.font_medium.render(f"Wynik: {self.score}", True, BLACK)
        drinks_text = self.font_medium.render(f"Drinki: {self.drinks_made}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(drinks_text, (10, 40))

        # Instrukcje z ostrzeżeniem o mieszaniu
        inst_text = self.font_small.render("Trzymaj butelkę aby nalewać!", True, BLACK)
        self.screen.blit(inst_text, (650, 50))

        inst2_text = self.font_tiny.render("MUSISZ wstrząsnąć shakerem aby wymieszać!", True, RED)
        self.screen.blit(inst2_text, (650, 75))

        inst3_text = self.font_tiny.render("Za dużo wstrząśnięć = kara punktowa", True, ORANGE)
        self.screen.blit(inst3_text, (650, 95))

        # Butelki składników
        for bottle in self.ingredient_bottles:
            bottle.draw(self.screen, self.ingredient_images)

        # Shaker
        self.shaker.draw(self.screen)

        # Przyciski
        self.shake_button.draw(self.screen)
        self.serve_button.draw(self.screen)
        self.clear_button.draw(self.screen)
        self.menu_button.draw(self.screen)

        # Zawartość shakera - bez procentów, tylko lista
        if self.shaker.contents:
            contents_text = self.font_small.render("W shakerze:", True, BLACK)
            self.screen.blit(contents_text, (400, 550))

            y_offset = 570
            for ingredient in self.shaker.contents.keys():
                if self.shaker.contents[ingredient] > 0.01:  # Tylko widoczne ilości
                    content_text = self.font_tiny.render(f"• {ingredient}", True, BLACK)
                    self.screen.blit(content_text, (400, y_offset))
                    y_offset += 18

    def draw_result(self):
        self.screen.fill(WHITE)

        if not self.last_result:
            return

        # Tytuł wyniku
        result_text = self.font_large.render("WYNIK DRINKU", True, BLACK)
        result_rect = result_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.screen.blit(result_text, result_rect)

        # Wiadomość
        message_text = self.font_medium.render(self.last_result['message'], True, BLACK)
        message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(message_text, message_rect)

        # Punkty z bonusem za mieszanie
        points_text = self.font_medium.render(f"Punkty: +{self.last_result['points']}", True, GREEN)
        points_rect = points_text.get_rect(center=(SCREEN_WIDTH // 2, 140))
        self.screen.blit(points_text, points_rect)

        # Szczegóły mieszania
        if 'base_points' in self.last_result:
            base_text = self.font_small.render(f"Punkty bazowe: {self.last_result['base_points']}", True, BLACK)
            self.screen.blit(base_text, (50, 180))

            mixing_bonus = self.last_result['mixing_bonus']
            bonus_color = GREEN if mixing_bonus >= 0.9 else ORANGE if mixing_bonus >= 0.7 else RED
            mixing_text = self.font_small.render(f"Mnożnik mieszania: {mixing_bonus:.2f}", True, bonus_color)
            self.screen.blit(mixing_text, (50, 200))

            shake_text = self.font_small.render(f"Ilość wstrząśnięć: {self.last_result['shake_count']}", True, BLACK)
            self.screen.blit(shake_text, (50, 220))

            if not self.last_result['was_mixed']:
                warning_text = self.font_small.render("Drink nie był wymieszany!", True, RED)
                self.screen.blit(warning_text, (50, 240))

        # Podobieństwo
        similarity = self.last_result['similarity']
        similarity_text = self.font_small.render(f"Podobieństwo do przepisu: {similarity:.1%}", True, BLACK)
        self.screen.blit(similarity_text, (50, 270))

        # Najlepsze dopasowanie
        if self.last_result['match']:
            match = self.last_result['match']
            match_text = self.font_medium.render(f"Najbliżej do: {match.name}", True, BLUE)
            match_rect = match_text.get_rect(center=(SCREEN_WIDTH // 2, 320))
            self.screen.blit(match_text, match_rect)

            # Opis drinku
            desc_text = self.font_small.render(match.description, True, BLACK)
            desc_rect = desc_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
            self.screen.blit(desc_text, desc_rect)

            # Porównanie składników
            comparison_text = self.font_small.render("Porównanie składników:", True, BLACK)
            self.screen.blit(comparison_text, (50, 390))

            y_offset = 420
            player_drink = self.last_result['player_drink']

            # Wszystkie składniki z obu drinków
            all_ingredients = set(player_drink.keys()) | set(match.ingredients.keys())

            for ingredient in sorted(all_ingredients):
                player_amount = player_drink.get(ingredient, 0) * 100
                recipe_amount = match.ingredients.get(ingredient, 0) * 100

                if player_amount > 0 or recipe_amount > 0:
                    comp_text = self.font_tiny.render(
                        f"{ingredient}: Ty {player_amount:.0f}% vs Przepis {recipe_amount:.0f}%",
                        True, BLACK
                    )
                    self.screen.blit(comp_text, (50, y_offset))
                    y_offset += 20

        # Statystyki gracza
        if self.player_name:
            player_text = self.font_small.render(f"Gracz: {self.player_name}", True, BLACK)
            self.screen.blit(player_text, (50, SCREEN_HEIGHT - 100))

        stats_text = self.font_small.render(f"Całkowity wynik: {self.score} | Drinki: {self.drinks_made}", True, BLACK)
        self.screen.blit(stats_text, (50, SCREEN_HEIGHT - 80))

        # Przyciski
        self.continue_button.draw(self.screen)
        self.menu_button.draw(self.screen)

    def run(self):
        running = True

        while running:
            running = self.handle_events()
            self.update()

            if self.state == GameState.MENU:
                self.draw_menu()
            elif self.state == GameState.PLAYING:
                self.draw_game()
            elif self.state == GameState.RESULT:
                self.draw_result()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game = BartenderGame()
    game.run()