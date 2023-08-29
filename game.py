import sys
import time

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

        """设定初始方向，具体可以在设置类里面改"""
        self.direction = self.settings.direction

        """导入屏幕帧数函数"""
        self.clock = pygame.time.Clock()
    def run_game(self):
        while True:
            self.check_event()
            self.update_screen()


    def check_event(self):
        """定义事件检查函数，如果检测到单击了关闭按钮，退出游戏"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    self.direction = "UP"
                elif event.key == pygame.K_LEFT:
                    self.direction = "LEFT"
                elif event.key == pygame.K_DOWN:
                    self.direction = "DOWN"

    def update_screen(self):
        """定义更新屏幕函数"""

        """填充屏幕颜色，颜色选项在设置类中"""
        self.screen.fill(self.settings.bg_color)
        """绘制蛇头"""
        self.snakepart.blitsnakehead()
        """绘制蛇的移动"""
        self.move_snake()
        """设定帧率"""
        self.clock.tick(30)

        """刷新屏幕"""
        pygame.display.flip()

    def move_snake(self):
        """定义一个控制蛇移动方向的函数"""
        if self.direction == "RIGHT":
            self.snakepart.rect.x += 3
        elif self.direction == "LEFT":
            self.snakepart.rect.x -= 3
        elif self.direction == "DOWN":
            self.snakepart.rect.y += 3
        elif self.direction == "UP":
            self.snakepart.rect.y -= 3




if __name__ == '__main__':
    glusnake = Game()
    glusnake.run_game()