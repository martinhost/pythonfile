#第一个游戏
import pygame 
import sys

pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请多多关照！")

turtle = pygame.image.load("turtle.png")
tur = pygame.transform.scale(turtle, (90, 90))

position = tur.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    position = position.move(speed)

    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(tur, True, False)
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    screen.fill(bg)
    screen.blit(tur, position)
    pygame.display.flip()
    pygame.time.delay(10)

