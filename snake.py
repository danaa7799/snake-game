import pygame
import random

# initialize pygame
pygame.init()

# define game window dimensions
WIDTH, HEIGHT = 600, 600

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# define snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
snake_speed = 10

# define food properties
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawned = True

# define clock
clock = pygame.time.Clock()

# define font
font_style = pygame.font.SysFont(None, 50)


# function to display message on screen
def message(msg, color):
    message_text = font_style.render(msg, True, color)
    screen.blit(message_text, [WIDTH / 6, HEIGHT / 3])


# game loop
game_over = False
while not game_over:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                snake_direction = "LEFT"
            elif event.key == pygame.K_UP:
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake_direction = "DOWN"

    # move snake
    if snake_direction == "RIGHT":
        snake_pos[0] += snake_speed
    elif snake_direction == "LEFT":
        snake_pos[0] -= snake_speed
    elif snake_direction == "UP":
        snake_pos[1] -= snake_speed
    elif snake_direction == "DOWN":
        snake_pos[1] += snake_speed

    # snake body mechanics
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawned = False
    else:
        snake_body.pop()

    # food mechanics
    if not food_spawned:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawned = True

    # draw screen
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # border mechanics
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over = True

    # body collision mechanics
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over = True

    # update display
    pygame.display.update()

    # set game FPS
    clock.tick(20)

# display game over message
message("Game Over")
