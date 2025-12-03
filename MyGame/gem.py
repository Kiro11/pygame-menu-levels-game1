import pygame
YELLOW = (255,255,0)

class Gem:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)
