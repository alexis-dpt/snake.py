import pygame
import time
import random

Créateur = "alexis_dpt_on_github"
print(Créateur)

pygame.init()

blue = (0, 0, 255)
light_blue = (20, 20, 255)
green = (56, 178, 56)
light_green = (50, 161, 50)
red = (255, 0, 0)
window_width = 800
window_height = 600

game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Jeu du serpent V1| Crée par alexis_dpt 🤓💻')

snake_speed = 12
snake_block = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 35)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, blue if x == snake_list[-1] else light_blue, [x[0], x[1], snake_block, snake_block])

def display_loose_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 3, window_height / 5])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 10, window_height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, window_height - snake_block) / 20.0) * 20.0

    start_time = time.time()

    direction = ''

    while not game_over:
        while game_close:
            game_window.fill(green)
            display_loose_message("Tu as perdu!", red)
            display_message("Appuie sur A pour quitter ou E pour rejouer", blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'DOWN'

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        for i in range(0, window_width, 20):
            color = green if (i // 20) % 2 == 0 else light_green
            pygame.draw.rect(game_window, color, [i, 0, 20, window_height])

        pygame.draw.rect(game_window, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)

        elapsed_time = time.time() - start_time
        score = length_of_snake - 1
        value = font_style.render(f"Score: {score} Temps: {int(elapsed_time)}s", True, red)
        game_window.blit(value, [0, 0])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, window_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
