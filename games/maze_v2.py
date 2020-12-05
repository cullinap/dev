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

class End(object):

    def __init__(self, pos):
        ends.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

pygame.init()

pygame.display.set_caption("Maze game")
screen = pygame.display.set_mode((340, 260))

clock = pygame.time.Clock()
walls = []
ends = []
player = Player()

level = [
    "WWEWWWWWWWWWWWWWWWWWW",
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
    "W     W        W    W",
    "WWWWWWWWWWWWWWWWWWWWW",
]

x = y = 0

for row in level:
    for col in row:
        if col == "W":
            Wall((x,y))
        if col == "E":
            End((x,y))
            #end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

i = 0

running = True
while running:

    clock.tick(5)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    
    #x = random.randint(0,3)
    if i < 12:
        x = 2
    elif i < 130:
        x = 1
    elif i < 131:
        x = 3
    elif 213 >= i >= 210:
        x = 0
    elif i == 214:
        x = 2
    elif 259 >= i > 215:
        x = 0
    elif i == 260:
        x = 3

    print(i,x)
    i+=1
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

    
    #for wall in walls:
    #    if player.rect.colliderect(pygame.rect(0,5,16,16)):

    #        print('collide')
    #        raise SystemExit
        #print(wall.rect[0], wall.rect[1])



    # Just added this to make it slightly fun ;)
    for end in ends:
        if player.rect.colliderect(end.rect):
            raise SystemExit 
    
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for end in ends:
        pygame.draw.rect(screen, (255, 0, 0), end.rect)

    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()



















































