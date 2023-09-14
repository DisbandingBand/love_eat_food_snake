import pygame
from setting import Settings
from pygame.sprite import Sprite

class SnakeBlock(Sprite):

    def __init__(self,game):
        super().__init__()
        self.settings = Settings()
        self.screen = game.screen

        self.color = self.settings.snakeheadcolor

        self.rect = pygame.Rect(0,0,self.settings.snakeblockwidth,self.settings.snakeblockheight)
        self.rect.x = 400
        self.rect.y = 300
        self.x = self.rect.x
        self.y = self.rect.y

        self.direction = self.settings.direction
        self.double_speed = False


    def draw_block(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        """定义一个控制蛇移动方向的函数"""
        if self.direction == "RIGHT":
            """检测是否有双倍速率"""
            if self.double_speed == True:
                self.x += self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.x += self.settings.speed
        elif self.direction == "LEFT":
            if self.double_speed == True:
                self.x -= self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.x -= self.settings.speed
        elif self.direction == "DOWN":
            if self.double_speed == True:
                self.y += self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.y += self.settings.speed
        elif self.direction == "UP":
            if self.double_speed == True:
                self.y -= self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.y -= self.settings.speed


        self.rect.x = self.x
        self.rect.y = self.y