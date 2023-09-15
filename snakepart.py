import sys

import pygame
from setting import Settings


class SnakePart:



    def __init__(self,game):
        """主要是对蛇的一些属性的配置，并且需要导入形参来获得屏幕属性"""
        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.snakeheadcolor = (15,48,135)
        self.direction = self.settings.RIGHT
        self.double_speed = False
        self.snakebody_rect = [pygame.Rect(0,0,0,0)] * 4
        self.snakehead_rect = pygame.Rect(0,0,20,20)
        self.game_over = False

    def drawsnakebody(self):
        for i in self.snakebody_rect:
            pygame.draw.rect(self.screen,(255,255,0),i)
    def drawsnakehead(self):
        pygame.draw.rect(self.screen,self.snakeheadcolor,self.snakehead_rect)

    def _update(self):

        """把蛇身添加到列表第一个，并删除列表最后一个"""
        self.snakebody_rect = [self.snakehead_rect] + self.snakebody_rect
        self.snakebody_rect.pop()
        print(self.snakebody_rect)

        """蛇头碰撞到身体则失败，关闭游戏"""
        for j in self.snakebody_rect[1:]:
            if j == self.snakehead_rect:
                self.game_over = True
        if self.game_over == True:
            sys.exit()

        """上下左右可通过"""
        if self.snakehead_rect.left > self.screen_rect.right:
            self.snakehead_rect.left = self.screen_rect.left
        elif self.snakehead_rect.right < self.screen_rect.left:
            self.snakehead_rect.right = self.screen_rect.right
        elif self.snakehead_rect.top > self.screen_rect.bottom:
            self.snakehead_rect.top = self.screen_rect.top
        elif self.snakehead_rect.bottom < self.screen_rect.top:
            self.snakehead_rect.bottom = self.screen_rect.bottom


    def move_snake(self):
        """定义一个控制蛇移动方向的函数"""

        self.snakehead_rect = self.snakehead_rect.move(self.direction)

