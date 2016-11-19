# Кириллов Алексей, ИУ7-12
# Вычислить определённый интеграл, используя метод Монте-Карло и правило Уэддля

from random import random

def f(x):   # Функция f(x); задаётся при проверке
    return x*x

def fperv(x):   # Первообразная функции; задаётся при проверке
    return x**3/3

def integral(a,b):  # Определённый интеграл по первообразной
    return abs(fperv(b) - fperv(a))

def maxf(a,b,n):    # Нахождение верхней границы для метода М-К
    maxy = f(a)
    k = a
    step = (b-a)/n
    while k <= (b+step/4):
        if f(k) >= maxy:
            maxy = f(k)*(1+1/n)
        k += step
    return maxy

def format_i(intg):    # Форматирование числа для вывода
    strg = str(abs(intg))
    if 'e' in strg:    # Если число уже в экспоненциальной форме
        strg = strg[:(10-len(strg)+strg.index('e')\
                      if (10-len(strg)+strg.index('e')) >9\
                    else 10)]+ strg[strg.index('e'):]
    elif len(strg) < 10:    # Если число короче 10 символов
        if intg%1 == 0:
            strg = strg + ' '*(10 - len(strg))
        else:
            strg = strg + '0'*(10 - len(strg))
    else:
        if '.' not in strg:    # Экспонента для целых чисел
            if strg[0] == '1':
                strg = '1.'+strg[1:9]+'e+'+str(len(strg)-1)
            else:
                strg = '0.'+strg[:8]+'e+'+str(len(strg))
        else:   # Экспонента для вещественных чисел
            if strg.index('.') > 9:
                strg = strg[:10]
                if strg[0] == '1':
                    strg = '1.'+strg[1:9]+'e+'+str(len(strg)-1)
                else:
                    strg = '0.'+strg[:8]+'e+'+str(len(strg))
            elif strg.index('.') == 9:
                strg = strg[:9] + ' '
            else:
                strg = strg[:10]
    strg = '-'+strg if intg<0 else ' '+strg    # Возврат знака
    return strg

print('Функция f(x) = x*x, первообразная = x*x*x/3')
a,b = map(float,input('Задайте границы параметра функции(х): ').split())
delta = b - a

print('\nНахождение интеграла по формуле Уэддля использует промежутки, \
их число кратно 6\n')

z = list(map(int,input('Задайте число разбиений (2 числа): ').split()))

if z[0]%6 != 0 and z[1]%6 != 0:
    print('Некорректное число разбиений: невозможно применить формулу Уэддля')
elif z[0]%6 != 0 or z[1]%6 != 0:
    print('Формула Уэддля неприменима в одном случае: разбиение не кратно 6')

print('\nНахождение интеграла методом Монте-Карло использует случайные \
подстановки точек\n')

k = list(map(int,input('Введите количество подстановок (2 числа): ').split()))

maxy = maxf(a,b,max(k))
integrals = [[0,0],[0,0],[0,0]]

for h in range(2):

    # Метод Монте-Карло:
    npr = 0
    for i in range(k[h]):
        if f(a+random()*delta) >= random()*maxy:
              npr += 1
              
    integrals[0][h] = maxy*delta*npr/k[h]
    #print('Используя метод Монте-Карло:\t',integrals[0][h])

    if z[h]%6 == 0:
        n = z[h]//6
        step = delta/z[h]
        
        # Формула Уэддля:
        L = [f(a)]*7
        I2 = 0

        for i in range(n):
            L[0] = L[6]
            for j in range(1,7):
                L[j] = f(a+step*(6*i+j))
            I2 += L[0] + 5*L[1] + L[2] + 6*L[3] + L[4] + 5*L[5] + L[6]
        
        integrals[1][h] = I2*3*step/10
    #print('По формуле Уэддля: \t\t',integrals[1][h])

# Вывод таблицы значений:
print('\nВычисленные значения интеграла:\n')
print('     метод:\t {:<4} и {:<4}\t {:<4} и {:<4}'.format(k[0],z[0],
                                                           k[1],z[1]))
print('Монте-Карло\t{:}\t{:}'.format(format_i(integrals[0][0]),
                                     format_i(integrals[0][1])))
print('     Уэддля\t',end='')
if integrals[1][0] == 0:
    print(' невычислим\t',end='')
else:
    print('{:}\t'.format(format_i(integrals[1][0])),end='')
if integrals[1][1] == 0:
    print(' невычислим')
else:
    print('{:}'.format(format_i(integrals[1][1])))
integrals[2][0] = integral(a,b)
print('\nИнтеграл по первообразной = {:}'.format(format_i(integrals[2][0])))

# Нахождение минимального необходимого количества разбиений:
eps = float(input('\nЗадайте точность для определения необходимого количества \
итераций\nметода Монте-Карло для нахождения интеграла с заданой точностью: '))
print()
npr = n = 1
while True:
    np = n
    npr *= 2
    for i in range(npr//2+1):
        if f(a+random()*delta) >= random()*maxy:
            n += 1
    if abs(maxy*delta*n/npr - integrals[2][0]) <= eps:
        integrals[2][1] = maxy*delta*n/npr
        if npr <= 8:
            print('Точность достигута за',npr,'операций; возможно, погрешность\
                  \nгенератора случайных чисел; найдём следующее значение.')
            continue
        print('Предыдущее значение:',format_i(maxy*delta*2*np/npr))
        break
# Нахождение погрешностей и окончательный вывод:
print('После',npr,'итераций метод Монте-Карло достиг необходимой точности;')
print('Его значение = {:}'.format(format_i(integrals[2][1])))
#integrals[2][0] = wp
integrals[2][1] = abs(integrals[2][1] - integrals[2][0])
print('Абсолютная погрешность = {:}'.format(format_i(integrals[2][1])))
if integrals[2][0]!=0:
    integrals[2][0] = integrals[2][1]/integrals[2][0]
    print('Относительная = {:}'.format(format_i(integrals[2][0])))
else:
    print('Относительная погрешность неопределена, т.к. интеграл = 0')
