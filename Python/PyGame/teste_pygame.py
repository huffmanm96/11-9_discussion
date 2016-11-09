import pygame
import time

def keyboardHandler(event):
    global gameRun
    global lead_x_change
    global lead_y_change
    global block_size

    if(event.type == pygame.QUIT):
        gameRun = False

    if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_ESCAPE):
            gameRun = False
        elif(event.key == pygame.K_LEFT):
            lead_x_change = - block_size
            lead_y_change = 0
        elif(event.key == pygame.K_RIGHT):
            lead_x_change = block_size
            lead_y_change = 0
        elif(event.key == pygame.K_UP):
            lead_y_change = - block_size
            lead_x_change = 0
        elif(event.key == pygame.K_DOWN):
            lead_y_change = block_size
            lead_x_change = 0

def gameControl():
    return

def message_to_screen(msg, color):
    global display_width
    global display_height

    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])
    pygame.display.update()

##########
# VARIAVEIS
##########
red = 0
green = 0
blue = 255
color = (red, green, blue)

display_width = 600
display_height = 600

gameRun = True

lead_x = display_width / 2
lead_y = display_height / 2

lead_x_change = 0
lead_y_change = 0

block_size = 10

fps = 10

##########
# MAIN
##########
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

while (gameRun):
    pygame.display.update()

    for event in pygame.event.get():
        # EXIT Handler
        print(event)
        keyboardHandler(event)

    if( lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0):
        gameRun = False

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill((255, 0, 0))
    pygame.draw.rect(gameDisplay, (color), [lead_x, lead_y, block_size, block_size])
    # gameDisplay.fill(color, [0, 0, 10, 10])

    # pygame.display.update()
    clock.tick(fps)

message_to_screen("You Lose", (255, 255, 255))
time.sleep(2)
pygame.quit()
quit()

# I changed the block color in the middle from blue to red, and the words at the end from red to blue.

