import pygame

# initialize pygame
pygame.init()

# open a window and set dimensions
screen = pygame.display.set_mode((340,240))

# create an instance of the time method
clock = pygame.time.Clock()

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class End(object):

    def __init__(self, pos):
        ends.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

level = [
    "WWWWEWWWWWWWWWWWWWWWW",
    "W                   E",
    "W         WWWWWW    W",
    "W   WWWW       W    W",
    "W   W        WWWW   W",
    "W WWW  WWWW         W",
    "W   W     W W       W",
    "W   W     W   WWW  WW",
    "W   WWW WWW   W W   W",
    "W     W   W   W W   W",
    "WWW   W   WWWWW W   W",
    "W W      WW         W",
    "W W   WWWW   WWW    W",
    "W     W        W    W",
    "WWWWWWWWWWWWWWWWWWWWW",
]

walls = []
ends = []

x,y = 0,0

for row in level:
    for col in row:
        if col == "W":
            Wall((x,y))
        if col == "E":
            End((x,y))
        x += 16
    y += 16
    x = 0


running = True

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

player = Player()

# game loop
while running:
    
    for e in pygame.event.get(): #  user did something
        if e.type == pygame.QUIT: # if user closes windown
            running = False # stop the game loop
    
    # game logic here

    # fill the screen to white 
    # draw commands above will be erased
    screen.fill((0,0,0))

    # draw some stuff hre
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)

    for end in ends:
        pygame.draw.rect(screen, (255, 0,0 ), end.rect)

    pygame.draw.rect(screen, (255, 200, 0), player.rect)
        
    # update the screen with what was drawn
    pygame.display.flip()


    # set frames per second
    clock.tick(20)

pygame.quit()

