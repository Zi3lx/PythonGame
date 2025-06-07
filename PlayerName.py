import pygame
from Constants import *

class PlayerNameInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 32)
        self.text = ""
        self.active = False
        self.cursor_visible = True
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return True  # Enter pressed
            elif len(self.text) < 12 and event.unicode.isprintable():
                self.text += event.unicode

        return False

    def update(self):
        self.cursor_timer += 1
        if self.cursor_timer >= 30:  # Blink every 30 frames
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

    def draw(self, screen):
        # Input box
        color = BLUE if self.active else GRAY
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, color, self.rect, 2)

        # Text
        display_text = self.text
        if self.active and self.cursor_visible:
            display_text += "|"

        text_surface = self.font.render(display_text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))