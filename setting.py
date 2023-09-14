import random

import pygame

"""创建设置类"""
class Settings:



    def __init__(self):
        """对屏幕设置在这一块"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        """对蛇的设置在这一块"""
        self.snakeblockwidth = 20
        self.snakeblockheight = 20
        self.snakeheadcolor = (15,48,135)

        """控制类设置"""
        self.direction = "RIGHT"
        self.speed = 10
        self.speed_multiple = 2

        """食物类设置"""
        self.foodwidth = 20
        self.foodheight = 20
        self.foodcolor = (255,0,0)

    def generatefoodpos(self):
        x = random.randrange(0, self.screen_width - self.foodwidth)
        y = random.randrange(0, self.screen_height - self.foodheight)
        position = (x, y)
        return position
