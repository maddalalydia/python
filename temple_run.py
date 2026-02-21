import pygame
import random

pygame.init()

# Screen
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Temple Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

clock = pygame.time.Clock()

# Player
player = pygame.Rect(100, 300, 40, 60)
velocity = 0
gravity = 1
jump_power = -15

# Obstacle
obstacle = pygame.Rect(800, 320, 40, 40)
speed = 7

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Jump
    if keys[pygame.K_SPACE] and player.bottom >= 360:
        velocity = jump_power

    velocity += gravity
    player.y += velocity

    if player.bottom >= 360:
        player.bottom = 360

    obstacle.x -= speed
    if obstacle.x < -40:
        obstacle.x = 800
        score += 1

    if player.colliderect(obstacle):
        print("Game Over! Score:", score)
        running = False

    pygame.draw.line(screen, BLACK, (0, 360), (800, 360), 3)
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, obstacle)

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
