import pygame
from setting import Settings


class FoodPart:



    def __init__(self,game):
        self.settings = Settings()
        self.screen = game.screen

        self.foodsquare = pygame.Surface(self.settings.foodsize)
        self.foodsquare.fill(self.settings.foodcolor)

    def blitfood(self):
        """定义一个函数，用于绘制蛇的图像"""
        self.screen.blit(self.foodsquare,(580,160))