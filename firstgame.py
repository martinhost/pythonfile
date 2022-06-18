#第一个游戏
import pygame 
import sys

#初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)

#创建指定大小的窗口
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption("初次见面，请多多关照！")

#调用图片
turtle = pygame.image.load("turtle.png")
tur = pygame.transform.scale(turtle, (90, 90))#改写图片尺寸大小
#获得图像的位置矩形
position = tur.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        #翻转图像
        turtle = pygame.transform.flip(tur, True, False)
        #反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(tur, position)
    #更新界面
    pygame.display.flip()
    #延时10ms
    pygame.time.delay(10)

