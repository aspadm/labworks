# Кириллов Алексей, ИУ7-12
# Защита(График): нарисовать график функции на отрезке [a,b] с шагом h.
# Отобразить нулевую линию по необходимости.

from math import sin

try:
    a,b,h = map(float,input('Введите границы отрезка и шаг: ').split())
    
    maxy = miny = 0
    n = 61

    t = a    
    while t<=(b+h/2):
        y = 0.5 - sin(t)
        t += h
        if y > maxy or maxy == 0: maxy = y
        if y < miny or miny == 0: miny = y

    delt = maxy - miny

    if miny <= 0 <= maxy:
        pos = int(round((-miny)*n/delt))
    else:
        pos = -1

    print(' '*5,end='')
    print('{:^11.5g}'.format(miny),end='')
    print(' '*49,end='')
    print('{:^11.5g}'.format(maxy))
    
    print(' '*10,end='')
    for i in range(n):
        if i==pos:
            print('+',end='')
        else:
            print('-',end='')
    print('>')

    t = a
    while t<=(b+h/2):
        if abs(t)<h/3: t=0
        y = int(round((0.5 - sin(t) -miny)*n/delt))
        print('{:8.5g}: '.format(t),end='')
        for i in range(n+1):
            if i == y:
                print('*',end='')
            elif i == pos:
                print('|',end='')
            else:
                print(' ',end='')
        print()
        t+=h

except ValueError:
    print('Ошибка значений!')
