import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pat's game")

done = False

# instantiate an instance of Clock class
clock = pygame.time.Clock()

game_room = [[[0,10],[20,10]],
             [[0,20],[20,20]]
            ]

# main program loop
while not done:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # game logic here

    # first clear the screen to white
    # if you want a background image replace with blit'ing
    screen.fill(WHITE)

    # drawing code here
    for i in range(2):
        # print(game_room[i][0], game_room[i][1])
        pygame.draw.line(screen, RED, game_room[i][0], game_room[i][1], 5)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("My text", True, BLACK)
    screen.blit(text, [250, 250])

    # update the screen with what we've drawn
    pygame.display.flip()

    # limit 60 frames per second
    clock.tick(60)

pygame.quit()
