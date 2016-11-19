# Кириллов Алексей, ИУ7-12
# Исследование алгоритма Монте-Карло на одинаковой выборке

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

print('Функция f(x) = x*x, первообразная = x*x*x/3')
a,b = map(float,input('Задайте границы параметра функции(х): ').split())
delta = b - a
maxy = maxf(a,b,1000)
print('Максимум функции =',maxy)
k,n = map(int,input('Введите кол-во итераций и число проверок:').split())

s = 0
for j in range(n):
    npr = 0
    for i in range(k):
        if f(a+random()*delta) >= random()*maxy:
              npr += 1
    s += maxy*delta*npr/k
    print('Прогон:',j,'значение =',maxy*delta*npr/k)
s /= n
print(s,integral(a,b),abs(s-integral(a,b)))
