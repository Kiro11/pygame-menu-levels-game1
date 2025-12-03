import pygame
RED = (255,0,0)

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed_x = 3
        self.speed_y = 3

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
