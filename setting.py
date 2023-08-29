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
        self.snakespeed = 5
