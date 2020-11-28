import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode([400,400])

pygame.display.set_caption("Maze")

clock = pygame.time.Clock()

x = 50
y = 50
width = 40
height = 60
vel = 5

player_rect = pygame.Rect(50, 50, 40, 60)

#walls = [
#    pygame.Rect(300, 0, 20, 100),
#    pygame.Rect(200, 0, 20, 100)
#]


class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

def move_player(x_speed, y_speed):

    move_axis_and_check(player_rect, x_speed, 0)

    move_axis_and_check(player_rect, 0, y_speed)

def move_axis_and_check(rect, x_speed, y_speed):
    rect.x += x_speed
    rect.y += y_speed

    for wall in walls:
        if rect.colliderect(wall):

            if x_speed > 0:
                rect.right = wall.left

            elif x_speed < 0:
                rect.left = wall.right

            if y_speed > 0:
                rect.bottom = wall.top

            if y_speed < 0:
                rect.top = wall.bottom

walls = []

levels = [
    "WWWWWWWWWWW",
    "W         W",
    "WWWWWWWWWWW"
]

x,y = 0,0

for row in levels:
    for col in row:
        if col == "W":
            Wall((x,y))
        x+=16
    y+=16
    x = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        move_player(-2, 0)
    if keys[pygame.K_RIGHT] and x < 350:
        move_player(2, 0)
    if keys[pygame.K_UP] and y > vel:
        move_player(0, -2)
    if keys[pygame.K_DOWN] and y < 350:
        move_player(0, 2)

    player_rect.clamp_ip(screen.get_rect())

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player_rect)

    for wall in walls:
        pygame.draw.rect(screen, RED, wall.rect)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()




