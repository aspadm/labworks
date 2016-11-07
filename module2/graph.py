# Кириллов Алексей, ИУ7-12

# Вывести таблицу значений функций, построить график одной из них.
# Так же определить суммы отрицательных значений функций.
# Для цикла используется конструкция "while"

from math import cos, pi

try:
    x0, h, xm = map(float,input('Введите х0, прирост, максимум: ').split())
    s1 = s2 = 0
    min2 = max2 = 5*x0**3 + 2*x0*x0 - 15*x0 - 6
        
    x = x0-h
    print('\nt          \tp1          \tp2\t')
    while x<xm:
        x+=h
        y1 = x - cos(pi*x)
        y2 = 5*x**3 + 2*x*x - 15*x - 6
        if y2>max2: max2=y2
        if y2<min2: min2=y2
        if y1<0: s1+=y1
        if y2<0: s2+=y2
        
        print('{:-0.4g}\t\t{:<10.8g}\t{:<10.8g}'.format(x,y1,y2))

    print()

    print('Сумма отрицательных р1 = {:0.8g}, р2 = {:0.8f}\n'.format(s1,s2))
    print('Минимум и максимум функции: {:0.8g} и {:0.8g}\n'.format(min2,max2))

    pos = -1
    if min2 <= 0 <= max2:
        pos = round((- min2)/(max2 - min2)*56)
        #print(pos)

    print('{:>10.4g} '.format(min2)," "*55,' {:<10.4g}'.format(max2),sep='')
    print(" "*11,end='')
    for i in range(56):
        if i==pos:
            print('+',end='')
        else:
            print('-',end='')
    print('>')
    

    x = x0-h
    while x<xm:
        x+=h
        y2 = 5*x**3 + 2*x*x - 15*x - 6
        y2 = round((y2 - min2)/(max2 - min2)*56)
        print('{:>10.4g} '.format(x),end='')
        for i in range(57):
            if y2==i: print('*',end='')
            elif pos==i: print('|',end='')
            else: print(' ',end='')
        print()

except ValueError:
    print('Ошибка типов!')
