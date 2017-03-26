# Кириллов Алексей, ИУ7-22
# Защита уточнений корней, метод секущих

from math import sin

def f(x):
    #return x*2-4
    return 5*sin(x)

a, b = map(float, input('Задайте границы отрезка: ').split())
eps = float(input('Задайте точность по х: '))
max_iter = int(input('Максимальное число итераций: '))

if (f(a) >= 0 and f(b) >= 0) or (f(a) < 0 and f(b) < 0):
    print('Невозможно вычислить: некорректные границы, f(a)=',f(a),'f(b)=',f(b))

x0, x1 = a,b
x = a
iter_count = 0

while abs(x1 - x0) > eps:
    if iter_count == max_iter:
        print('Значение не найдено за',max_iter,'итераций')
        break
    
    x = x1 - ((f(x1)*(x1-x0))/(f(x1) - f(x0)))
    print(iter_count,x)
    
    if x > b or x < a:
        print('Касательная указывает за пределы интервала ({:5.6}), \
найти корень невозможно'.format(x))
        break

    x0 = x1
    x1 = x
 
    iter_count += 1

eps_real = abs(x1 - x0)
if eps_real <= eps:

    print('Корень найден за {:} итераций, x = {:5.6f}; \
f(x) = {:2.1g}, погрешность = {:2.1g}'.format(iter_count, x, f(x) ,eps_real))
