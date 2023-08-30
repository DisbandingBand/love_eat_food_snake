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

        # self.foodrect.x = self.settings.generatefoodpos()[0]
        # self.foodrect.y = self.settings.generatefoodpos()[1]

        while True:
            self.foodrect.x = self.settings.generatefoodpos()[0]
            self.foodrect.y = self.settings.generatefoodpos()[1]
            if not self.snakepart.snakehead_rect.colliderect(self.foodrect):
                break
        print("Snake head rect:", self.snakepart.snakehead_rect)
        print("Food rect:", self.foodrect)


    def drawfood(self):
        pygame.draw.rect(self.screen,self.color,self.foodrect)

    def iseatfood(self):
        # if self.snakepart.snakehead_rect.colliderect(self.foodrect) == True: 只在实例化执行了一次，之后不会再执行
        print("test：碰到了")
        self.foodrect.x = self.settings.generatefoodpos()[0]
        self.foodrect.y = self.settings.generatefoodpos()[1]
