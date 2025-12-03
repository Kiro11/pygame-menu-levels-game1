import pygame
import sys
from player import Player
from enemy import Enemy
from gem import Gem
from menu import menu_screen, game_over_screen

# ----------- إعداد Pygame -----------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))  # Windowed mode

pygame.display.set_caption("لعبتي Premium")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# ----------- ألوان -----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

# ----------- كائنات اللعبة -----------
player = Player(WIDTH//2, HEIGHT//2)
enemies = [Enemy(100,100), Enemy(700,100), Enemy(400,400)]
gems = [Gem(200,200), Gem(600,300), Gem(400,500)]
score = 0

# ----------- حلقة اللعبة الرئيسية -----------
def game_loop():
    global score
    running = True
    while running:
        screen.fill(GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)

        # رسم اللاعب
        player.draw(screen)

        # رسم الأعداء وتحريكهم
        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
            if player.rect.colliderect(enemy.rect):
                game_over_screen(game_loop)

        # رسم الجواهر والتحقق من جمعها
        for gem in gems[:]:
            gem.draw(screen)
            if player.rect.colliderect(gem.rect):
                gems.remove(gem)
                score += 10

        # عرض النقاط
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10,10))

        pygame.display.flip()
        clock.tick(60)

# ----------- التشغيل -----------
menu_screen()
game_loop()
game_loop