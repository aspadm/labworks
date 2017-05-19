# Кириллов Алексей, ИУ7-22
# Защита (PyGame)
# Поршневой насос надувает шарик, который затем улетает

import pygame
from pygame.locals import *
from math import cos, pi
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Protection")

clock = pygame.time.Clock()

radius = 0
step = 0
x = 400
y = 400
a_y = 1
while True:
    for event in pygame.event.get():
        if (event.type == QUIT) or\
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit(0)

    screen.fill((50,50,70))
    if radius < 100**2:
        angle = pi*step/20
        p_y = 480 - round(45*cos(angle))
        if cos(angle) > 0:
            radius += 35*cos(angle)
    pygame.draw.polygon(screen, (200,200,200), [(400,400),(430,430),
                                                (430,530),(370,530),
                                                (370,430)], 7)
    pygame.draw.polygon(screen, (170,170,170), [(400,400),(430,430),
                                                (430,530),(370,530),
                                                (370,430)])
    pygame.draw.polygon(screen, (210,210,210), [(370,p_y),(430,p_y),
                                                (430,p_y+10),(405,p_y+10),
                                                (405,p_y+120),(395,p_y+120),
                                                (395,p_y+10),(370,p_y+10)])

    if radius < 100**2:
        y = 400 - round(radius**(1/2))
    elif y > -radius:
        a_y *= 1.02
        y -= a_y
    pygame.draw.circle(screen, (250, 10, 10), (x, round(y)),
                       round(radius**(1/2)))

    step += 1
    pygame.display.flip()
    clock.tick(60)
    
