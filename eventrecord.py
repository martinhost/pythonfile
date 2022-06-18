import pygame
import sys

pygame.init()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Machang Demo")

f = open("eventrecord.txt", 'w')

while True:
    for event in pygame.event.get():
        f.write(str(event) + '\n')
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()
