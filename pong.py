import pygame, sys, random

def ballAnimation():
    global ballSpeedX, ballSpeedY

    # Ball movement
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Ball collisions with screen borders
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1

    if ball.left <= 0 or ball.right >= screenWidth:
        ballRestart()

    # Ball collisions with players
    if ball.colliderect(opponent) or ball.colliderect(player):
        ballSpeedX *= -1

def ballRestart():
    global ballSpeedX, ballSpeedY
    # Center the ball
    ball.center = (screenWidth/2, screenHeight/2)

    # Randomize travel direction
    ballSpeedX *= random.choice((1, -1))
    ballSpeedY *= random.choice((1, -1))

def playerAnimation():
    # Players movement
    player.y += playerSpeed
    
    # Out of bounds player check
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def opponentAi():
    # Opponent tracking
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    else:
        opponent.bottom -= opponentSpeed

    # Out of bounds opponent check
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

# Game rectangles
ballSize = 30
playerWidth = 10
playerHeight = 140
ball = pygame.Rect(screenWidth/2 - ballSize/2, screenHeight/2 - ballSize/2, ballSize, ballSize)
player = pygame.Rect(screenWidth - 2*playerWidth, screenHeight/2 - playerHeight/2, playerWidth, playerHeight)
opponent = pygame.Rect(playerWidth, screenHeight/2 - playerHeight/2, playerWidth, playerHeight)

# Colors
bgColor = pygame.Color('gray12')
lightGray = (200,200,200)

# Movement variables
ballSpeedX = 8 *= random.choice((1, -1))
ballSpeedY = 8 *= random.choice((1, -1))
playerSpeed = 0
playerAcceleration = 8
opponentSpeed = 8

while True:
    # Handling input
    for event in pygame.event.get():
        # Exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Up arrow key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += playerAcceleration
            if event.key == pygame.K_UP:
                playerSpeed -= playerAcceleration

        # Down arrow key pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= playerAcceleration
            if event.key == pygame.K_UP:
                playerSpeed += playerAcceleration

    # Ball movement and collisions
    ballAnimation()

    # Player's (right) movement and collisions
    playerAnimation()

    # Opponent's tracking and collisions
    opponentAi()

    # Visuals
    screen.fill(bgColor)
    pygame.draw.rect(screen, lightGray, player)
    pygame.draw.rect(screen, lightGray, opponent)
    pygame.draw.ellipse(screen, lightGray, ball)
    pygame.draw.aaline(screen, lightGray, (screenWidth/2,0), (screenWidth/2,screenHeight))
    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)