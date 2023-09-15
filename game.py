import sys
import pygame
from setting import Settings
from snakepart import SnakePart
from foodpart import FoodPart


class Game:



    def __init__(self):
        pygame.init()
        """导入设置类，对于屏幕或者蛇的什么设置可以放在这里"""
        self.settings = Settings()
        """绘制屏幕，长宽比在设置类中"""
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        """导入蛇的部分类，对于蛇头和蛇身的设置可以放在这里，这里因为需要导入屏幕，所以要放在self.screen的后面"""


        self.snakepart = SnakePart(self)
        self.foodpart = FoodPart(self)

        """导入屏幕帧数函数"""
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self.check_event()

            self.snakepart.move_snake()
            self.snakepart._update()

            self.update_screen()


    def check_event(self):
        """定义事件检查函数，如果检测到单击了关闭按钮，退出游戏"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                """检测按键，上下左右"""
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snakepart.direction != self.settings.LEFT:
                    self.snakepart.direction = self.settings.RIGHT
                elif event.key == pygame.K_UP and self.snakepart.direction != self.settings.DOWN:
                    self.snakepart.direction = self.settings.UP
                elif event.key == pygame.K_LEFT and self.snakepart.direction != self.settings.RIGHT:
                    self.snakepart.direction = self.settings.LEFT
                elif event.key == pygame.K_DOWN and self.snakepart.direction != self.settings.UP:
                    self.snakepart.direction = self.settings.DOWN
                elif event.key == pygame.K_SPACE:
                    self.snakepart.double_speed = True





    def update_screen(self):
        """定义更新屏幕函数"""

        """填充屏幕颜色，颜色选项在设置类中"""
        self.screen.fill(self.settings.bg_color)

        self.snakepart.drawsnakebody()
        self.snakepart.drawsnakehead()
        """设定帧率"""
        self.clock.tick(5)
        """刷新屏幕"""
        pygame.display.flip()





if __name__ == '__main__':
    glusnake = Game()
    glusnake.run_game()