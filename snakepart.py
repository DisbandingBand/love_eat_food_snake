import pygame
from setting import Settings


class SnakePart:



    def __init__(self,game):
        """主要是对蛇的一些属性的配置，并且需要导入形参来获得屏幕属性"""

        """导入设置类"""
        self.settings = Settings()

        """获得game中的屏幕，并使用方法访问屏幕的rect"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        """设置蛇头的属性，数值在设置类中"""
        self.snakehead = pygame.Surface(self.settings.snakeheadsquare)
        self.snakehead.fill(self.settings.snakeheadcolor)

        """访问蛇头的rect，并让蛇头的中心等于屏幕的中心"""
        self.rect = self.snakehead.get_rect()
        self.rect.center = self.screen_rect.center

        """设定初始方向，具体可以在设置类里面改"""
        self.direction = self.settings.direction
        self.double_spped = False
    def blitsnakehead(self):
        """定义一个函数，用于绘制蛇的图像"""
        self.screen.blit(self.snakehead,self.rect)

    def move_snake(self):
        """定义一个控制蛇移动方向的函数"""
        if self.direction == "RIGHT":
            """检测是否有双倍速率"""
            if self.double_spped == True:
                self.rect.x += self.settings.speed * self.settings.speed_multiple
            elif self.double_spped == False:
                self.rect.x += self.settings.speed
        elif self.direction == "LEFT":
            if self.double_spped == True:
                self.rect.x -= self.settings.speed * self.settings.speed_multiple
            elif self.double_spped == False:
                self.rect.x -= self.settings.speed
        elif self.direction == "DOWN":
            if self.double_spped == True:
                self.rect.y += self.settings.speed * self.settings.speed_multiple
            elif self.double_spped == False:
                self.rect.y += self.settings.speed
        elif self.direction == "UP":
            if self.double_spped == True:
                self.rect.y -= self.settings.speed * self.settings.speed_multiple
            elif self.double_spped == False:
                self.rect.y -= self.settings.speed

        if self.rect.left > self.screen_rect.right:
            self.rect.right = self.screen_rect.left
            self.screen.blit(self.snakehead,self.rect)
        elif self.rect.right < self.screen_rect.left:
            self.rect.left = self.screen_rect.right
            self.screen.blit(self.snakehead,self.rect)
        elif self.rect.top > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.top
            self.screen.blit(self.snakehead,self.rect)
        elif self.rect.bottom < self.screen_rect.top:
            self.rect.top = self.screen_rect.bottom
            self.screen.blit(self.snakehead,self.rect)