import pygame
from setting import Settings


class SnakePart:



    def __init__(self,game):
        """主要是对蛇的一些属性的配置，并且需要导入形参来获得屏幕属性"""

        """导入设置类"""
        self.setting = Settings()

        """获得game中的屏幕，并使用方法访问屏幕的rect"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        """设置蛇头的属性，数值在设置类中"""
        self.snakehead = pygame.Surface(self.setting.snakeheadsquare)
        self.snakehead.fill(self.setting.snakeheadcolor)

        """访问蛇头的rect，并让蛇头的中心等于屏幕的中心"""
        self.rect = self.snakehead.get_rect()
        self.rect.center = self.screen_rect.center

    def blitsnakehead(self):
        """定义一个函数，用于绘制蛇的图像"""
        self.screen.blit(self.snakehead,self.rect)