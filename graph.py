# Кириллов Алексей, ИУ7-12

# Вывести таблицу значений функций, построить график одной из них.
# Так же определить суммы отрицательных значений функций.
# Для цикла используется конструкция "while"

from math import cos, pi

try:
    x0, h, xm = map(float,input('Введите х0, прирост, максимум: ').split())
    s1 = s2 = 0
    min2 = 5*x0**3 + 2*x0*x0 - 15*x0 - 6
    max2 = 0
        
    x = x0-h
    print('\nt       \tp1         \tp2\t')
    while x<xm:
        x+=h
        y1 = x - cos(pi*x)
        y2 = 5*x**3 + 2*x*x - 15*x - 6
        if y2>max2: max2=y2
        if y2<min2: min2=y2
        if y1<0: s1+=y1
        if y2<0: s2+=y2
        
        print('{:0.4f}  \t{:0.8f}  \t{:0.8f}'.format(x,y1,y2))

    print()

    print('Сумма отрицательных р1 = {:0.8f}, р2 = {:0.8f}\n'.format(s1,s2))
    print(min2,max2)

    print('{:7.4} '.format(min2),'-'*61,'>',' {:7.4}'.format(max2),sep="")

    x = x0-h
    while x<xm:
        x+=h
        y2 = 5*x**3 + 2*x*x - 15*x - 6
        y2 = round((y2 - min2)/(max2 - min2)*61)
        #print(y2)
        print('{:0.4f} '.format(x),end='')
        for i in range(62):
            if y2==i: print('*',end='')
            else: print(' ',end='')
        print()
    #if max2*min2 <=0
    
except ValueError:
    print('Ошибка типов!')
