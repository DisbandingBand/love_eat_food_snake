import pygame

import random
pygame.init()
clock = pygame.time.Clock()
# 游戏窗口大小
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))


x = window_width / 2
y = window_height / 2
aalist = [[x,y]]

while True:
    pygame.display.update()
    x -= 1
    window.fill((0,0,0))
    for i in aalist:
        pygame.draw.rect(window, (155, 155, 155), [i[0],i[1], 20, 20])
# 控制游戏帧率
    clock.tick(10)
