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
        self.snakeheadsquare = (20,20)
        self.snakeheadcolor = (15,48,135)

        """控制类设置"""



        self.UP, self.DOWN, self.LEFT, self.RIGHT = (0, -20), (0, 20), (-20, 0), (20, 0)
        """食物类设置"""
        self.foodwidth = 20
        self.foodheight = 20
        self.foodcolor = (255,0,0)

    def generatefoodpos(self):
        x = random.randrange(0,800,20)
        y = random.randrange(0,600,20)
        position = (x,y)

        return position

