import pygame
import random
import sys

class Car:
    HEIGHT = 800
    WIDTH = 1000

    WALL_HEIGHT = 20
    WALL_WIDTH = 5

    COLOUR = (255, 255, 255)

    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock() 
        self.central_wall = pygame.Rect(self.WIDTH / 2, 200, 10, 400)
        self.west_wall = pygame.Rect(200, 200, 10, 400)

    def game_loop(self):
        i = 20

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                     return
            
            self.screen.fill((0,0,0))
            
            pygame.draw.rect(self.screen, self.COLOUR, self.central_wall)
            pygame.draw.rect(self.screen, self.COLOUR, self.west_wall)

            pygame.draw.line(self.screen, self.COLOUR, (0,i), (20, i))

            if i > 600:

            
            pygame.display.flip()
            
            self.clock.tick(60)


if __name__ == '__main__':
    car = Car()
    car.game_loop()





