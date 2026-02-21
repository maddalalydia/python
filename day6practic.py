#check weather the num is armstrong or not
'''num = int(input())
temp = num
digits = len(str(num))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")'''

#perfect num
'''n = int(input())
original = n
i = 1
total = 0
while i <= n // 2:
    if n % i == 0:
        total += i
    i += 1
if total == original:
    print("Perfect Number")
else:
    print("Not a Perfect Number")'''

# a game
'''import random
print("🎮 Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it in", attempts, "attempts.")
        break'''

#xox game
'''board = [" " for _ in range(9)]
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False
current_player = "X"
while True:
    print_board()
    move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
    if board[move] == " ":
        board[move] = current_player
        if check_winner(current_player):
            print_board()
            print("🎉 Player", current_player, "wins!")
            break
        if " " not in board:
            print_board()
            print("It's a Draw!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Position already taken! Try again.") '''

'''import random
board = [" " for _ in range(9)]
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False
def computer_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_positions)
current_player = "X"
while True:
    print_board()

    if current_player == "X":
        move = int(input("Your move (1-9): ")) - 1
        
        if board[move] != " ":
            print("Position already taken! Try again.")
            continue
    else:
        move = computer_move()
        print("Computer chose position:", move + 1)
    board[move] = current_player
    if check_winner(current_player):
        print_board()
        if current_player == "X":
            print("🎉 You win!")
        else:
            print("🤖 Computer wins!")
        break
    if " " not in board:
        print_board()
        print("It's a Draw!")
        break
    current_player = "O" if current_player == "X" else "X" '''

#temple run
'''import random
import time

print("🏃 Welcome to Temple Runner!")
print("Press:")
print("  j → Jump")
print("  s → Slide")
print("  r → Run")
print("Avoid obstacles and survive!\n")

score = 0
game_over = False

actions = ["j", "s", "r"]
obstacles = ["jump", "slide", "run"]

while not game_over:
    obstacle = random.choice(obstacles)
    print("\n⚠ Obstacle ahead! You must:", obstacle.upper())
    
    player_move = input("Your move (j/s/r): ").lower()
    
    if (obstacle == "jump" and player_move == "j") or \
       (obstacle == "slide" and player_move == "s") or \
       (obstacle == "run" and player_move == "r"):
        score += 10
        print("✅ Good move! Score:", score)
    else:
        print("💀 You hit the obstacle!")
        game_over = True

    time.sleep(1)

print("\n🏁 Game Over! Final Score:", score)'''

import pygame
import random

# Initialize
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

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Jump
    if keys[pygame.K_SPACE] and player.bottom >= 360:
        velocity = jump_power

    # Gravity
    velocity += gravity
    player.y += velocity

    if player.bottom >= 360:
        player.bottom = 360

    # Move obstacle
    obstacle.x -= speed
    if obstacle.x < -40:
        obstacle.x = 800
        score += 1

    # Collision
    if player.colliderect(obstacle):
        print("Game Over! Score:", score)
        running = False

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, 360), (800, 360), 3)

    # Draw player & obstacle
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, obstacle)

    # Score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()


