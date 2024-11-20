import pygame
import time
import random
from highscore_manager import save_highscore, load_highscore

pygame.init()

width = 800
height = 600

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block = 10
snake_speed = 15

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

pygame.mixer.init()
pygame.mixer.music.load("music/music.mp3")  # Bakgrundsmusik
pygame.mixer.music.play(-1)  # Loopa musiken
move_sound = pygame.mixer.Sound("music/move.mp3")
food_sound = pygame.mixer.Sound("music/food.mp3")
gameover_sound = pygame.mixer.Sound("music/gameover.mp3")

apple_image = pygame.image.load("img/apple.jpg")
apple_image = pygame.transform.scale(apple_image, (10, 10))  # Anpassa storlek till 10x10

def our_score(score):
    value = score_font.render(f"Your Score: {score}", True, yellow)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    highscore = load_highscore()
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            pygame.mixer.music.stop()
            gameover_sound.play()
            message("You Lost! Press C-Play Again or Q-Quit", red)
            our_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        pygame.mixer.music.play(-1)  # Starta musiken igen
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    move_sound.play()
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    move_sound.play()
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    move_sound.play()
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    move_sound.play()

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        screen.blit(apple_image, (foodx, foody))

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        our_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            food_sound.play()

        clock.tick(snake_speed)

    if length_of_snake - 1 > highscore:
        save_highscore(length_of_snake - 1)

    pygame.quit()
    quit()
