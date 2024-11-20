import pygame

from snake_logic import gameLoop
from highscore_manager import load_highscore

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game with Highscore and Music')

highscore = load_highscore()

def start_screen():
    font = pygame.font.SysFont("bahnschrift", 35)
    screen.fill((0, 0, 0))
    title = font.render("Welcome to Snake Game!", True, (255, 255, 255))
    instruction = font.render("Press SPACE to start the game", True, (255, 255, 255))
    highscore_display = font.render(f"Highest score: {highscore}", True, (255, 255, 0))
    screen.blit(title, (width // 4, height // 3))
    screen.blit(instruction, (width // 4, height // 2))
    screen.blit(highscore_display, (width // 4, height // 1.5))
    pygame.display.update()

def main():
    start_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameLoop()
    pygame.quit()

if __name__ == "__main__":
    main()