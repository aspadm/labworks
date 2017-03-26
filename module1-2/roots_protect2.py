# Кириллов Алексей, ИУ7-22
# Защита уточнений корней, метод касательных

from math import sin, cos

def f(x):
    #return x*2-4
    return sin(x)

def fs(x):
    return cos(x)

a, b = map(float, input('Задайте границы отрезка: ').split())
eps = float(input('Задайте точность по х: '))
max_iter = int(input('Максимальное число итераций: '))

if (f(a) >= 0 and f(b) >= 0) or (f(a) < 0 and f(b) < 0):
    print('Невозможно вычислить: некорректные границы, f(a)=',f(a),'f(b)=',f(b))

x = a
xprev = b
iter_count = 0

while abs(xprev - x) > eps:
    if iter_count == max_iter:
        print('Значение 1 не найдено за',max_iter,'итераций')
        break

    xprev = x
    x = x - f(x)/fs(x)
    #print(iter_count,x)
    
    if x > b or x < a:
        print('Касательная 1 указывает за пределы интервала({:5.6})'.format(x))
        break

    iter_count += 1

eps_real = abs(xprev - x)
if eps_real <= eps:

    print('Корень найден за {:} итераций, x = {:5.6f}; \
f(x) = {:2.1g}, погрешность = {:2.1g}'.format(iter_count, x, f(x) ,eps_real))

else:
    x = b
    xprev = a
    iter_count = 0

    while abs(xprev - x) > eps:
        if iter_count == max_iter:
            print('Значение 2 не найдено за',max_iter,'итераций')
            break

        xprev = x
        x = x - f(x)/fs(x)
        #print(iter_count,x)
        
        if x > b or x < a:
            print('Касательная 2 указывает за пределы интервала({:5.6})'.format(x))
            break

        iter_count += 1

    eps_real = abs(xprev - x)
    if eps_real <= eps:

        print('Корень найден за {:} итераций, x = {:5.6f}; \
f(x) = {:2.1g}, погрешность = {:2.1g}'.format(iter_count, x, f(x) ,eps_real))
