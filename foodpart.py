import pygame
from setting import Settings
from snakepart import SnakePart


class FoodPart:



    def __init__(self,game):
        self.settings = Settings()
        self.screen = game.screen
        self.snakepart = SnakePart(game)

        self.foodrect = pygame.Rect(0,0,self.settings.foodwidth,self.settings.foodheight)
        self.color = self.settings.foodcolor

        self.foodrect.x = self.settings.generatefoodpos()[0]
        self.foodrect.y = self.settings.generatefoodpos()[1]

    def drawfood(self):
        pygame.draw.rect(self.screen,self.color,self.foodrect)

    def iseatfood(self):
        if self.snakepart.snakehead_rect.contains(self.foodrect) == True:
            self.foodrect.x = self.settings.generatefoodpos()[0]
            self.foodrect.y = self.settings.generatefoodpos()[1]
