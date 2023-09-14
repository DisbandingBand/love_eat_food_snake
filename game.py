import pygame
import sys
class Game:



    def __init__(self):
        pygame.init()
        screen_width = 800
        screen_height = 600
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.bg_color = (230,230,230)
        self.snake_x = screen_width / 2
        self.snake_y = screen_height / 2
        self.snakelist = [[self.snake_x,self.snake_y]]
        self.snakeblockcolor = (15,48,135)
        self.direction = 'RIGHT'
        self.clock = pygame.time.Clock()
        self.speed = 20
    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"
                    elif event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"


            if self.direction == 'LEFT':
                self.snake_x -= self.speed
            elif self.direction == 'RIGHT':
                self.snake_x += self.speed
            elif self.direction == 'UP':
                self.snake_y -= self.speed
            elif self.direction == 'DOWN':
                self.snake_y += self.speed

            self.screen.fill(self.bg_color)

            for i in self.snakelist:
                pygame.draw.rect(self.screen,self.snakeblockcolor,[i[0],i[1],20,20])

            self.clock.tick(10)
            pygame.display.flip()



if __name__ == '__main__':
    glusnake = Game()
    glusnake.run_game()