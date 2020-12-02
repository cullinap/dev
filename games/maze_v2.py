import pygame
import random

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        
        if dx != 0:
            self.move_single_axis(dx, 0)

        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

pygame.init()

pygame.display.set_caption("Maze game")
screen = pygame.display.set_mode((340, 260))

clock = pygame.time.Clock()
walls = []
player = Player()

level = [
    "WWWWWWWWWWWWWWWWWWWWW",
    "W                   W",
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
    "W     W    E   W    W",
    "WWWWWWWWWWWWWWWWWWWWW",
]

x = y = 0

for row in level:
    for col in row:
        if col == "W":
            Wall((x,y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    
    x = random.randint(0,3)
    
    if x == 0:
        player.move(-2,0)
    if x == 1:
        player.move(2,0)
    if x == 2:
        player.move(0,-2)
    if x == 3:
        player.move(0,2)



    #key = pygame.key.get_pressed()
    #if key[pygame.K_LEFT]:
    #    player.move(-2, 0)
    #if key[pygame.K_RIGHT]:
    #    player.move(2, 0)
    #if key[pygame.K_UP]:
    #    player.move(0, -2)
    #if key[pygame.K_DOWN]:
     #   player.move(0, 2)
    
    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        raise SystemExit 
    
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()


















































