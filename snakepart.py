import pygame
from setting import Settings
from pygame.sprite import Sprite

class SnakePart:



    def __init__(self,game):
        """主要是对蛇的一些属性的配置，并且需要导入形参来获得屏幕属性"""

        """导入设置类"""
        self.settings = Settings()

        """获得game中的屏幕，并使用方法访问屏幕的rect"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        """设置蛇头的属性，数值在设置类中"""
        self.snake_x = self.settings.screen_width / 2
        self.snake_y = self.settings.screen_height / 2
        """访问蛇头的rect，并让蛇头的中心等于屏幕的中心"""
        self.snakehead = pygame.Surface((self.snake_x,self.snake_y))
        self.snakehead.fill(self.settings.snakeheadcolor)
        self.snakehead_rect = self.snakehead.get_rect()
        """设定初始方向，具体可以在设置类里面改"""
        self.direction = self.settings.direction
        self.double_speed = False


    def blitsnakehead(self):
        """定义一个函数，用于绘制蛇的图像"""
        pygame.draw.rect(self.screen,self.settings.snakeheadcolor,self.snakehead_rect)

    def move_snake(self):
        """定义一个控制蛇移动方向的函数"""
        if self.direction == "RIGHT":
            """检测是否有双倍速率"""
            if self.double_speed == True:
                self.snake_x += self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.snake_x += self.settings.speed
        elif self.direction == "LEFT":
            if self.double_speed == True:
                self.snake_x -= self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.snake_x -= self.settings.speed
        elif self.direction == "DOWN":
            if self.double_speed == True:
                self.snake_y += self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.snake_y += self.settings.speed
        elif self.direction == "UP":
            if self.double_speed == True:
                self.snake_y -= self.settings.speed * self.settings.speed_multiple
            elif self.double_speed == False:
                self.snake_y -= self.settings.speed

        if self.snakehead_rect.left > self.screen_rect.right:
            self.snakehead_rect.right = self.screen_rect.left
            pygame.draw.rect(self.screen,self.settings.snakeheadcolor,self.snakehead_rect)
        elif self.snakehead_rect.right < self.screen_rect.left:
            self.snakehead_rect.left = self.screen_rect.right
            pygame.draw.rect(self.screen,self.settings.snakeheadcolor,self.snakehead_rect)
        elif self.snakehead_rect.top > self.screen_rect.bottom:
            self.snakehead_rect.bottom = self.screen_rect.top
            pygame.draw.rect(self.screen,self.settings.snakeheadcolor,self.snakehead_rect)
        elif self.snakehead_rect.bottom < self.screen_rect.top:
            self.snakehead_rect.top = self.screen_rect.bottom
            pygame.draw.rect(self.screen,self.settings.snakeheadcolor,self.snakehead_rect)


    def update_snake(self):
        self.snakehead_rect.x = self.snake_x
        self.snakehead_rect.y = self.snake_y

