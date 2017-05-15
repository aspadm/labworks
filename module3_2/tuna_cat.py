# Шибанова Дарья, ИУ7-22
# Лабораторная работа "Использование PyGame"
# По полке ходит кот, изредка сталкивая с неё посуду.
# Управление: пробел - кот скоро остановится и сядет;
# цифры от 1 до 3 - следующая полка, на которую пойдёт кот;
# клавиша r - принудительно отразит кота по горизонтали;
# крестик в правом верхнем углу или escape - выход.

import pygame, sys
from pygame.locals import *
from random import randint
from math import sin

# Инициализация окна
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Котя портит сервиз")

step = 0

# Загрузка изображений
sprite = pygame.image.load('tuna_anim.png').convert_alpha()
sprite_sit = pygame.image.load('tuna_anim2.png').convert_alpha()
sprite_vase = pygame.image.load('vases.png').convert_alpha()

# Настройка полок
shelf = [130, 290, 470]
vases = []

# Генерация посуды на полках
for i in range(10):
    for j in range(3):
        if randint(0, 20) > 7:
            x = i*80
            y = shelf[j] - 140
            vase = sprite_vase.subsurface((randint(0, 4)*75, 0, 75, 150))
            vases.append([x, y, vase, False, 1])

# Инициализация параметров сцены
clock = pygame.time.Clock()
offset = 0
cat_x = 0
cat_y = shelf[0]-90
cat_sit = False
cat_must_sit = False
left_right = True
next_shelf = 2

# Основной цикл
while True:
    for event in pygame.event.get():
            # Выход из программы
            if (event.type == QUIT) or\
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                print("Выполнен выход")
                pygame.quit()
                sys.exit(0)
            # Кот сядет после нажатия пробела
            if (event.type == KEYDOWN and event.key == K_SPACE):
                cat_must_sit = True
                print("КОТЯ, ХВАТИТ!!!")
            # Принудительная смена направления клавишей r
            if (event.type == KEYDOWN and event.key == K_r):
                left_right = not left_right
            # Принудительный выбор следующей полки
            if (event.type == KEYDOWN and event.key == K_1):
                next_shelf = 0
            if (event.type == KEYDOWN and event.key == K_2):
                next_shelf = 1
            if (event.type == KEYDOWN and event.key == K_3):
                next_shelf = 2


    screen.fill((200,255,200)) # заливка фона белым

    # Отрисовка полок
    pygame.draw.line(screen, (190,90,120), (0,shelf[0]), (800,shelf[0]), 27)
    pygame.draw.line(screen, (110,90,40), (0,shelf[1]), (800,shelf[1]), 35)
    pygame.draw.line(screen, (190,100,60), (0,shelf[2]), (800,shelf[2]), 29)


    if step%3 == 0: # каждый третий кадр
        offset = step//3 % 12 * 100 # находим смещение для 1 из 12 кадров

    if step > 400 and not cat_sit: # если кот не сидит и ушёл за экран
        step = 0 # пусть идёт заново
        left_right = not left_right # и в другую сторону
        cat_y = shelf[next_shelf]-90 # и на случайной полке
        next_shelf = randint(0, 2) # в следующий раз - эта полка
        print("А потом котя полезет на полку", next_shelf+1)

    if cat_sit: # решил посидеть - пусть сядет и сидит
        offset = (step - sit_start)//3 * 100 # определение смещения кадра
        if offset >= 500: # если уже сидит
            offset = 500
    else: # иначе - пусть идёт
        if left_right:
            cat_x = -200 + 4*step
        else:
            cat_x = 800 - 4*step

    # Определение момента, когда кот усядется
    if (offset == 300) and cat_must_sit and not cat_sit and (0 < cat_x < 600):
        offset = 0
        sprite = sprite_sit
        cat_sit = True
        sit_start = step

    cat = sprite.subsurface((0, offset, 200, 100)) # выбираем часть атласа
    if left_right: # отражаем, если идёт слева направо
        cat = pygame.transform.flip(cat, True, False)
    screen.blit(cat, (cat_x, cat_y)) # лепим котиков на экран

    # Рисование ваз на экране
    for vase in vases:
        # Падающие вазы
        if vase[3] and vase[1] < 600:
            vase[4] *= 1.1
            vase[1] += vase[4]
        # Кот пытается столкнуть вазу
        elif cat_x + 160 > vase[0] > cat_x - 45  and not cat_sit and\
             randint(0, 1000) > 980 and vase[1] == cat_y - 50:
            vase[3] = True
            angle = randint(5, 60) if not left_right else randint(-60, -5)
            vase[0] += 10*sin(angle)
            vase[2] = pygame.transform.rotate(vase[2], angle)
        # Вывод на экран результата
        screen.blit(vase[2], (vase[0], vase[1]))

    step += 1 # обновляем счётчик анимации
    
    pygame.display.flip() # обновление дисплея
    clock.tick(60) # принудительная установка 60 кадров в секунду
