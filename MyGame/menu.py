import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 60)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def menu_screen():
    while True:
        screen.fill(WHITE)
        draw_text("", font, BLACK, screen, WIDTH//2, HEIGHT//3)
        draw_text("Press ENTER to Start", font, BLUE, screen, WIDTH//2, HEIGHT//2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

def game_over_screen(restart_func):
    while True:
        screen.fill(WHITE)
        draw_text("Game Over!", font, (255,0,0), screen, WIDTH//2, HEIGHT//3)
        draw_text("Press R to Restart or Q to Quit", font, (0,0,0), screen, WIDTH//2, HEIGHT//2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_func()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
