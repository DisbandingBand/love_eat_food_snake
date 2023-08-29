import sys
import pygame
from setting import Settings
from snakepart import SnakePart

class Game:



    def __init__(self):
        pygame.init()
        """导入设置类，对于屏幕或者蛇的什么设置可以放在这里"""
        self.settings = Settings()
        """绘制屏幕，长宽比在设置类中"""
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        """导入蛇的部分类，对于蛇头和蛇身的设置可以放在这里，这里因为需要导入屏幕，所以要放在self.screen的后面"""
        self.snakepart = SnakePart(self)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            """填充屏幕颜色，颜色选项在设置类中"""
            self.screen.fill(self.settings.bg_color)
            """绘制蛇头"""
            self.snakepart.blitsnakehead()
            """刷新屏幕"""
            pygame.display.flip()


if __name__ == '__main__':
    glusnake = Game()
    glusnake.run_game()