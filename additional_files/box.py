import pygame
from pygame import *
from math import pi

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
DISPLAY = (SCREEN_WIDTH,SCREEN_HEIGHT)		# задаем размеры окна
											 
pygame.init()	# иницилиализируем pygame
screen = pygame.display.set_mode(DISPLAY)	# создаем окно
pygame.display.set_caption('Пример')		# даем название окну

#основной цикл программы, где происходит рисование
done = False

box_WIDTH = 50                  # ширина будки
box_HEIGHT = 75                 # высота будки

x = (SCREEN_WIDTH-box_WIDTH)//2
y = (SCREEN_HEIGHT-box_HEIGHT)//2


while not done:
    # обработка завершения работы программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # выход из цикла

    bg = Surface(DISPLAY)	    # создаем Surface с разрамерами окна
    bg.fill(Color("lightblue"))     # заливаем голубым цветом командой fill
    screen.blit(bg, (0,0))      # отображаем Surface с заливкой на основной
                                # холст в точке (0,0)

    box = Surface( (box_WIDTH, box_HEIGHT) )    # создаем Surface для будки
                                                # с ее размерами
                                                
    TRANSPARENT_COLOR = Color("#123456")   # определяем прозрачный цвет
    box.set_colorkey(TRANSPARENT_COLOR)    # задаем для surface прозрачный цвет 
    box.fill(TRANSPARENT_COLOR)            # заливаем surface прозрачным цветом

    pygame.draw.rect(box, Color("red"), Rect(0, 25, 50, 50), 0)
    # рисуем красный прямоугольник внутри Surface будки
    
    pygame.draw.polygon(box, Color("darkgreen"), ((0,25), (25, 0), (50, 25)), 0)
    # рисуем зеленый треугольник (крышу будки)
    
    pygame.draw.circle(box, Color("blue"), (25, 50), 10, 0)
    # рисуем синие окно середине будки радиусом 10 

    screen.blit(box, (x,y) )
    # помещаем Surface с будкой в середину основного холста

    # рисуем черную линию в середине экрана под прямоугольником
    pygame.draw.line(screen, Color("black"), (0, (SCREEN_HEIGHT+box_HEIGHT)//2),
                     (SCREEN_WIDTH, (SCREEN_HEIGHT+box_HEIGHT)//2), 5)

    # рисуем желтый эллипс над будкой
    pygame.draw.ellipse(screen, Color("yellow"),
                        Rect(SCREEN_WIDTH//2,50, 100,50), 0)
    
    # рисуем крусную дугу справа от будки
    pygame.draw.arc(screen, Color("brown"),
                    Rect(SCREEN_WIDTH-150,50, 100, 100), 3*pi/2, 2*pi, 3)
    
    # рисуем замкнутый набор линии слева от будки 
    pygame.draw.lines(screen, Color("black"), True,
                      ( (30,30), (50,50), (50, 60), (90, 80), (120, 50)),2)

    #отображаем все изменения на экране
    pygame.display.update()


# завершаем работу pygame
pygame.quit()           
