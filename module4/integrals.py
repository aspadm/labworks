# Кириллов Алексей, ИУ7-12
# Вычислить определённый интеграл, используя метод Монте-Карло и правило Уэддля

from random import random

def f(x):
    return(x)

a,b = map(float,input('Задайте границы параметра функции(х): ').split())
delta = b - a

print('\nНахождение интеграла по формуле Уэддля использует промежутки, \
их число кратно 6;')
n = list(map(int,input('Количество разбиений на 6(2 числа): ').split()))
step = [delta/n[0]/6,delta/n[1]/6]

print('\nНахождение интеграла методом Монте-Карло использует случайные \
подстановки точек;')
k = list(map(int,input('Введите количество подстановок(2 числа): ').split()))

maxy = f(b)
for h in range(2):
    npr = 0
    z = 5
    for i in range(k[h]):
        if f(random()*delta) >= random()*maxy:
              npr += 1
        '''elif i/k[h] > z/100:
            print(z,'% -',maxy*delta*npr/i)
            z += 5
        '''
    print('\nВычисленные значения интеграла:')

    I1 = maxy*delta*npr/k[h]    # Монте-Карло
    print('Используя метод Монте-Карло:\t',I1)

    L = [f(a)]*7
    I2 = 0

    for i in range(n[h]):
        L[0] = L[6]
        for j in range(1,7):
            L[j] = f(a+step[h]*(6*i+j))
        I2 += L[0] + 5*L[1] + L[2] + 6*L[3] + L[4] + 5*L[5] + L[6]
    
    I2 = I2*3*step[h]/10    # Weddle
    print('По формуле Уэддля: \t\t',I2)
