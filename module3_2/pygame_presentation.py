# Кириллов Алексей, ИУ7-22
# Модуль PyGame
# 0 - падение метеорита
# 1 - ядерный взрыв
# 2 - молнии бьют в бегающих человечков
# 3 - безжизненный пейзаж со снегом
# 4 - солнышко и травка
# 5 - ликующие человечки и салют

import sys
import pygame
from pygame.locals import *
from math import sin, cos, sqrt, pi
from random import randint

# Инициализация окна
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Program exams")

# Создаём таймер
clock = pygame.time.Clock()
choice = -1

# Список цветов фона
bg_color = [(255,  53,   0),
            (255,  53,   0),
            ( 40,  40,  40),
            (  5,   5,   5),
            (127, 199, 255),
            ( 40,  36,  55),
            ( 23,  77,   0)]

# летающие ручка с зачёткой
def wait_screen(step):
    angle = 7*sin(step/50)
    angle2 = 6*cos(step/40)
    zach2 = pygame.transform.rotate(zach, angle)
    screen.blit(zach2, (90 + 80*sin(step/30), 200 + 30*cos(step/20)))
    pen2 = pygame.transform.rotate(pen, angle2)
    screen.blit(pen2, (600 - 30*sin(step/120)*cos(step/30),
                       40 - 30*cos(step/70)))

# выставление отметки и плавная смена экрана
def change_loc(loc, step):
    if step > 650:
        return
    if step < 400:
        screen.fill(bg_color[-1])
    # плавное выцветание промежуточной сцены
    if step < 123:
        bg = pygame.Surface((800, 600))
        bg.fill((255, 255, 255))
        bg.set_alpha(255 - step*2)
        screen.blit(bg, (0, 0))

    # текст выставляемой оценки
    if loc == 0:
        text = "на комиссию"
    elif loc == 1:
        text = "неуд."
    elif loc == 2:
        text = "незач."
    elif loc == 3:
        text = "удовл."
    elif loc == 4:
        text = "зач."
    elif loc == 5:
        text = "отлично"

    if step < 370:
        # добавление оценки
        ntext = font.render(text, False, [10, 10, 200])
        ntext.set_alpha((step-150))
        zach2 = zach.copy()
        zach2.blit(ntext, [400, 55])

        # ручка и зачётка
        angle2 = 6*cos(step/40)
        zach2 = pygame.transform.rotate(zach2, 5)
        screen.blit(zach2, (100, 200))
        pen2 = pygame.transform.rotate(pen, angle2)
        screen.blit(pen2, (510 - 30*sin(step/120)*cos(step/30),
                           -15 - 10*cos(step/70)))
        
    # переход к новой сцене через плавную заливку и выцветание
    if step >= 400:
        bg = pygame.Surface((800, 600))
        bg.fill((55, 55, 55))
        bg.set_alpha(1055 - step*2)
        screen.blit(bg, (0, 0))
    elif step >= 350:
        bg = pygame.Surface((800, 600))
        bg.fill((255, 255, 255))
        bg.set_alpha((-350 + step)*5)
        screen.blit(bg, (0, 0))

# Падение астероида на город
def asteroid_city(step):
    if step == 0:
        ast[0] = 1100
        ast[1] = -200
    if step == 1000:
        global help_step
        help_step = 400
    if 400 < step:
    # падение астероида
        if not 900 < step < 1000:
            pygame.draw.rect(screen, Color("#d6b44d"),
                             Rect(0, 300, 600, 300), 0)
            pygame.draw.polygon(screen, Color("#23807e"),
                                ((500,300),(800,300),
                                 (800,600),(300,600)), 0)
        # Пока астероид не упал на город
        if step < 900:
            screen.blit(city, (10, 0))
            asteroid = pygame.transform.rotate(ast[2], step)
            screen.blit(asteroid, (ast[0]-asteroid.get_rect()[2]/2,
                               ast[1]-asteroid.get_rect()[3]/2))
            ast[0] -= 2
            ast[1] += 1
    change_loc(0, step)

# Испытания ядерной бомбы
def bomb(step):
    if step == 1000:
        global help_step
        help_step = 400
    pygame.draw.rect(screen, (85,89,79), Rect(0, 440, 800, 160), 0)
    if step > 650:
    # взрыв ядерной бомбы
        stage = (step-650)//10
        if stage > 24:
            return
        x = stage%5*320
        y = stage//5*232
        screen.blit(pygame.transform.scale(bomb1.subsurface((x,y),
                (320,232)), (800, 600)), (0, 0))
    else:
        # падение снаряда
        screen.blit(abomb, (380, -800+2*step))
    change_loc(1, step)     

# Гроза
def thunderstorm(step):
    global thund_id
    global thund
    if step == 1200:
        global help_step
        help_step = 400
    pygame.draw.rect(screen, (85,89,79), Rect(0, 240, 800, 360), 0)
    # Определяем кадр анимации и его смещение
    stage = step%70
    y = stage//9*85
    x = (stage-y*9)%9*45
    # Отрисовка человечков
    for i in range(len(stickmans)):
        # Случайные отклонения по высоте
        if randint(0, 1000)>970:
            stickmans[i][3] = randint(-1,1)
        # Если в человечка не бьёт молния - двигаем его
        if not (thund > 0 and thund_id == i):
            stickmans[i][0] += stickmans[i][2]
            stickmans[i][1] += 2*stickmans[i][3]
        # Время создать молнию
        if randint(0, 1000)>1200+thund:
            thund = 30
            thund_id = i
            stickmans[i][2] = -stickmans[i][2] + randint(1, 3)
            if stickmans[i][2] == 0:
                stickmans[i][2] = -3
        # Если человечек убежал за экран - пусть бежит в обратную сторону
        if stickmans[i][0] > 800 or stickmans[i][0] < -90:
            stickmans[i][2] *= -1
        if stickmans[i][1] > 500:
            stickmans[i][1] = 500
        elif stickmans[i][1] < 200:
            stickmans[i][1] = 200
        if stickmans[i][2] > 0:
            screen.blit(stickman.subsurface((x,y),(45,85)),
                        (stickmans[i][0],stickmans[i][1]))
        else: # отразим изображение, если бежит справа налево
            screen.blit(pygame.transform.flip(stickman.subsurface(
            (x,y),(45,85)), True, False), (stickmans[i][0],stickmans[i][1]))
        # Отрисовка молнии
        if thund > 0 and thund_id == i:
            screen.blit(light, (stickmans[i][0]-70,stickmans[i][1]-290))
    # Отрисовка ранее сгенерированных облаков
    for cloud in clouds:
        screen.blit(cloud[2], (cloud[0]+cloud[3]*sin(cloud[4] + step/30),
                               cloud[1]+cloud[3]*cos(cloud[4] + step/40)))
    thund -= 1
    change_loc(2, step)

# Снегопад
def lifeless(step):
    if step == 700:
        global help_step
        help_step = 400
    pygame.draw.rect(screen, (85,89,79), Rect(0, 240, 800, 360), 0)
    # Отрисовка снежинок
    for pict in snow:
        pygame.draw.circle(screen, (255,255,255), (pict[0],pict[1]), 3)
        pict[0] += randint(-4,4)
        pict[1] += randint(2,5)
        # Если улетает за пределы экрана, возвращаем
        if pict[0] > 805:
            pict[0] = 805
        elif pict[0] < -5:
            pict[0] = -5
        if pict[1] > 600:
            pict[1] = randint(-10,-3)
    # Отрисовка облаков
    for cloud in clouds:
        screen.blit(cloud[2], (cloud[0]+cloud[3]*sin(cloud[4] + step/50),
                               cloud[1]+cloud[3]*cos(cloud[4] + step/60)))
    change_loc(3, step)

# Солнце и травка
def sun_and_grass(step):
    if step == 1000:
        global help_step
        help_step = 400
    # Создаём солнце
    sun = pygame.Surface((120,120))
    sun.set_colorkey(Color("#FEFEFE"))
    sun.fill(Color("#FEFEFE"))
    # Добавляем лучи
    for i in range(15):
        lenth = randint(35,60)
        pygame.draw.line(sun,(240, 220, 100),(60,60),
                         (60 + lenth*cos(6.28/15*i),
                          60 - lenth*sin(6.28/15*i)), 4)
    pygame.draw.circle(sun, (245, 220, 100), (60,60), 30)
    # Вращаем и отображаем на экран
    sun = pygame.transform.rotate(sun,step)
    screen.blit(sun, (400-sun.get_rect()[2]/2,110-sun.get_rect()[3]/2))
    pygame.draw.rect(screen, (30,210,120), Rect(0, 240, 800, 360), 0)
    # Создаём и отрисовываем траву
    grass = pygame.Surface((40,45))
    grass.set_colorkey(Color("#FEFEFE"))
    grass.fill(Color("#FEFEFE"))
    grass_angle = pi/2 + pi/6*cos(step/100)
    pygame.draw.line(grass,(10,180,50),(20,40),(35*cos(grass_angle),
                                                35*(1-sin(grass_angle))), 3)
    for i in range(23):
        for j in range(9):
            #pygame.draw.arc(screen, (10,180,50),Rect((i+1)*40, 250+40*j,20, 20), 0, pi*step/(15*180))
            screen.blit(grass, (i*40+10, 230+40*j))
    change_loc(4, step)

# Праздник с салютом
def happiness(step):
    if step == 1000:
        global help_step
        help_step = 400
    pygame.draw.rect(screen, (30,70,40), Rect(0, 240, 800, 360), 0)
    # Отрисовываем кадр заранее сгенерированной анимации человечка
    for men in mans:
        screen.blit(man[step%60],(men[0],men[1]+20*cos(pi*step/30)))
    # Рисуем и отображаем салют
    for fire in fireworks:
        fires = pygame.Surface((150,150)).convert_alpha()
        fires.fill((254,254,254,0))
        pygame.draw.circle(fires, (fire_color[fire[3]][0],
                                   fire_color[fire[3]][1],
                                   fire_color[fire[3]][2],
                                   round(255*abs(sin(step/20+fire[2])))),
                           (75, 75),
                           round(75*abs(sin(step/20+fire[2]))))
        screen.blit(fires, (fire[0], fire[1]))
    change_loc(5, step)


# зачётка
zach = pygame.image.load("zach.jpg").convert_alpha()
# ручка
pen = pygame.Surface((20, 300))
pen.set_colorkey(Color("#FEFEFE")) # задаем для surface прозрачный цвет 
pen.fill(Color("#FEFEFE"))
pygame.draw.rect(pen, (0, 50, 235), Rect(2, 0, 16, 190), 0)
pygame.draw.rect(pen, (0, 0, 255), Rect(8, 280, 4, 20), 0)
pygame.draw.polygon(pen, (100, 100, 100), ((8,290), (12,290),
                                           (18,270), (2,270)), 0)
pygame.draw.rect(pen, (70, 70, 200), Rect(1, 190, 18, 80), 0)

# создаём астероид
ast = [1100, -200]
asteroid = pygame.Surface((200,200))
asteroid.set_colorkey(Color("#FEFEFE"))
asteroid.fill(Color("#FEFEFE"))
pygame.draw.polygon(asteroid, (147,134,109),
                    [(12,33),(147,26),(189,56),
                     (198, 120),(164,199),(105,170),(24,112)])
ast.append(asteroid)
# создаём город
city = pygame.Surface((600, 600))
city.set_colorkey(Color("#FEFEFE")) 
city.fill(Color("#FEFEFE"))
# генерируем дома
home = pygame.Surface((100, 400))
home.fill((230, 100, 67))
for i in range(4):
    for j in range(19):
        pygame.draw.rect(home, (0, 50, 235), Rect(i*20+12, j*20+10, 15, 15), 0)
city.blit(pygame.transform.scale(home, (80, 300)), (10, 100))
city.blit(pygame.transform.scale(home, (40, 205)), (290, 190))
city.blit(pygame.transform.scale(home, (50, 200)), (225, 290))
city.blit(home, (100, 200))

# бомба
abomb = pygame.Surface((20, 80))
abomb.set_colorkey(Color("#FEFEFE")) 
abomb.fill(Color("#FEFEFE"))
pygame.draw.polygon(abomb, (0,0,10),
                    [(0,0),(20,0),(20,50),(10,80),(0,50)])
# спрайтшит взрыва
bomb1 = pygame.image.load("bomb.png").convert_alpha()

# молния
thund = 0
thund_id = 0
light = pygame.image.load("light.png").convert_alpha()
# человечки (спрайтшит)
stickman = pygame.image.load("stickman.png").convert_alpha()
stickmans = []
for i in range(7):
    stickmans.append([randint(100,700),randint(200,500),
                      randint(2,4),randint(-1,1)])

# генерация облаков
clouds = []
for i in range(10):
    cloud = pygame.Surface((300,200))
    cloud.set_colorkey(Color("#FEFEFE"))
    cloud.fill(Color("#FEFEFE"))
    for j in range(randint(17-i,21-i)):
        pygame.draw.circle(cloud, (100+7*i,100+7*i,100+7*i),
                           (randint(40,260),randint(40,160)),
                           randint(25-i,40-i))
    clouds.append([randint(-100,600),randint(-50,40),cloud,
                   randint(2,10),randint(1, 10)])

# снег
snow = []
for i in range(100):
    snow.append([randint(-5,805), randint(-25, 600)])

# ликующий человечек (генерация покадровой анимации)
man = []
for i in range(60):
    angle = pi*sin((i-30)*pi/30)/3
    angle2 = pi*sin((i-30)*pi/60)/3
    man_gen = pygame.Surface((80,120))
    man_gen.set_colorkey(Color("#FEFEFE"))
    man_gen.fill(Color("#FEFEFE"))
    pygame.draw.line(man_gen,(50,50,50),(40,20),(40,90),3)
    pygame.draw.circle(man_gen,(150,150,150),(40,12),12)
    pygame.draw.line(man_gen,(80,80,80),(40,30),
                     (40+30*cos(angle),
                      30+30*sin(angle)),3)
    pygame.draw.line(man_gen,(80,80,80),(40,30),
                     (40-30*cos(angle),
                      30+30*sin(angle)),3)
    pygame.draw.line(man_gen,(70,70,70),(40,90),
                     (40+30*abs(sin(angle2)),
                      90+30*cos(angle2)),3)
    pygame.draw.line(man_gen,(70,70,70),(40,90),
                     (40-30*abs(sin(angle2)),
                      90+30*cos(angle2)),3)
    man.append(man_gen)
# ликующий человечек (координаты спавна)
mans = []
for i in range(7):
    mans.append([randint(10,710),randint(210,470)])

# салют
fireworks = []
for i in range(10):
    fireworks.append([randint(-50,725), randint(-25, 100),
                      pi*randint(0, 100)/90, randint(0,3)])
fire_color = [(255,10,10),(10,255,10),(10,10,255),(255,120,50)]

# инициализация шрифта
font = pygame.font.Font(None, 30)

# инициализация переменных основного цикла
anim_step = 0
help_step = 500
anim_stop = False

# Основной цикл
while True:
        for event in pygame.event.get():
            # Выход из программы
            if (event.type == QUIT) or\
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                print("End of program")
                pygame.quit()
                sys.exit(0)

            # Выбор с клавиатуры
            if event.type == pygame.KEYDOWN:
                # вывод справки
                if event.key == pygame.K_F1:
                    help_step = 400
                # приостановка счётчика анимации
                if event.key == pygame.K_SPACE:
                    anim_stop = not anim_stop
                # выбор сцены
                elif choice == -1:
                    if   event.key == pygame.K_0:
                        choice = 0
                        anim_step = 0
                    elif event.key == pygame.K_1:
                        choice = 1
                        anim_step = 0
                    elif event.key == pygame.K_2:
                        choice = 2
                        anim_step = 0
                    elif event.key == pygame.K_3:
                        choice = 3
                        anim_step = 0
                    elif event.key == pygame.K_4:
                        choice = 4
                        anim_step = 0
                    elif event.key == pygame.K_5:
                        choice = 5
                        anim_step = 0
                # возврат в лобби
                elif event.key == pygame.K_q:
                    print("Scene restarted")
                    choice = -1
                    anim_step = 0

        # Первичная заливка
        screen.fill(bg_color[choice])

        # Запуск функции отрисовки конкретной сцены
        if   choice == -1:
            help_text = "Press 0 - 5 key"
            wait_screen(anim_step)
            if anim_step == 0:
                help_step = 400
        else:
            help_text = "Press Q to restart"
        if   choice == 0:
            asteroid_city(anim_step)
        elif choice == 1:
            bomb(anim_step)
        elif choice == 2:
            thunderstorm(anim_step)
        elif choice == 3:
            lifeless(anim_step)
        elif choice == 4:
            sun_and_grass(anim_step)
        elif choice == 5:
            happiness(anim_step)

        # Вывод подсказки
        if help_step >= 0:
            htext = font.render(help_text, False, [255, 255, 255])
            if help_step <= 255:
                htext.set_alpha(help_step)
            screen.blit(htext, [30, 30])
            help_step -= 4*((help_step + 100)//help_step)

        # Сброс счётчика и сцены через 5 минут
        if anim_step >= 90000:
            anim_step = 0
            print("App restarted")
            choice = -1
            
        # Приостановка счётчика анимации
        if not anim_stop:
            anim_step += 1

        # Обмен экранных буферов
        pygame.display.flip()

        # Ограничение частоты смены кадров в 60 за секунду
        clock.tick(60)

        # Отображение реального FPS в заголовке
        caption = "Program exams - FPS: {:.2f}".format(clock.get_fps())
        pygame.display.set_caption(caption)
