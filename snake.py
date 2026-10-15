
import pygame
import random

pygame.init()

# Create the game window
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Snake Game")

clock = pygame.time.Clock()

# Snake and fruit
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)

fruit = (
    random.randrange(0, width, 20),
    random.randrange(0, height, 20)
)

score = 0
running = True
game_over = False

font = pygame.font.SysFont(None, 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    if not game_over:
        # Move the snake
        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )
        snake.insert(0, head)

        # Eat fruit and grow bigger
        if head == fruit:
            score += 1
            fruit = (
                random.randrange(0, width, 20),
                random.randrange(0, height, 20)
            )
        else:
            snake.pop()

        # Check for wall or self collision
        if (head[0] < 0 or head[0] >= width or
            head[1] < 0 or head[1] >= height or
            head in snake[1:]):
            game_over = True

    # Draw everything
    screen.fill((20, 20, 20))

    for part in snake:
        pygame.draw.rect(screen, (0, 200, 0),
                         (part[0], part[1], 20, 20))

    pygame.draw.rect(screen, (255, 0, 0),
                     (fruit[0], fruit[1], 20, 20))

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if game_over:
        message = font.render("Game Over!", True, (255, 255, 0))
        screen.blit(message, (230, 180))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
