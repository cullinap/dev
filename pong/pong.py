import pygame
import random
import sys

class Pong:
    HEIGHT = 800  
    WIDTH = 1000 

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    BALL_WIDTH = 20 
    BALL_VELOCITY = 5 

    COLOUR = (255, 255, 255)

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.central_line = pygame.Rect(self.WIDTH / 2, 0, 1, self.HEIGHT)
        self.GAME_FONT = pygame.font.Font('freesansbold.ttf', 30)

        self.paddles = []
        self.balls = []
        self.paddles.append(Paddle(
            self.BALL_VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.paddles.append(Paddle(
            self.BALL_VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2, 
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.balls.append(Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))
        
        self.left_score = 0
        self.right_score = 0
    
    
    def check_ball_hits_wall(self):
        for ball in self.balls:
            if ball.x > self.WIDTH or ball.x < 0:
                if ball.x > self.WIDTH:
                    self.left_score += 1
                if ball.x < 0:
                    self.right_score += 1

                ball.velocity = 5
                ball.angle = 0
                ball.x = 490
                ball.y = 390
                self.paddles[0].y = 350
                self.paddles[1].y = 350

                print(self.left_score, "", self.right_score)

                if self.left_score > 2:
                    print("right side won")
                    sys.exit(1)
                if self.right_score > 2:
                    print("left side wins")
                    sys.exit(1)


            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_ball_hits_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10,10)
                    break

    def draw_paddles(self):
        for paddle in self.paddles:
            paddle.move_paddle(self.HEIGHT)
            pygame.draw.rect(self.screen, self.COLOUR, paddle)

    def draw_balls(self):
        for ball in self.balls:
            ball.move_ball()
            pygame.draw.rect(self.screen, self.COLOUR, ball)


    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.screen.fill((0,0,0))

            self.draw_paddles()
            self.draw_balls()

            self.check_ball_hits_paddle()
            self.check_ball_hits_wall()

            pygame.draw.rect(self.screen, self.COLOUR, self.central_line)

            pygame.display.flip()
            self.clock.tick(60)

class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity

class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle

if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()












