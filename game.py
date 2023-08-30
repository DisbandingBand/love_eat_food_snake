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
        print("test:原神启动")
        while True:
            self.check_event()
            self.snakepart.move_snake()
            if self.snakepart.snakehead_rect.colliderect(self.foodpart.foodrect):
                # colliderect判断蛇头和食物是否发生碰撞
                self.foodpart.iseatfood()
            # self.iseatfood()
            self.update_screen()


    def check_event(self):
        """定义事件检查函数，如果检测到单击了关闭按钮，退出游戏"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                """检测按键，上下左右，空格加速"""
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snakepart.direction != "LEFT":
                    self.snakepart.direction = "RIGHT"
                elif event.key == pygame.K_UP and self.snakepart.direction != "DOWN":
                    self.snakepart.direction = "UP"
                elif event.key == pygame.K_LEFT and self.snakepart.direction != "RIGHT":
                    self.snakepart.direction = "LEFT"
                elif event.key == pygame.K_DOWN and self.snakepart.direction != "UP":
                    self.snakepart.direction = "DOWN"
                elif event.key == pygame.K_SPACE:
                    self.snakepart.double_spped = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.snakepart.double_spped = False


    def update_screen(self):
        """定义更新屏幕函数"""

        """填充屏幕颜色，颜色选项在设置类中"""
        self.screen.fill(self.settings.bg_color)
        """绘制蛇头"""
        self.snakepart.blitsnakehead()

        self.foodpart.drawfood()
        """设定帧率"""
        self.clock.tick(20)
        """刷新屏幕"""
        pygame.display.flip()


if __name__ == '__main__':
    glusnake = Game()
    glusnake.run_game()