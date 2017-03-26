# Кириллов Алексей, ИУ7-22
# Уточнение корней методом brenth

from math import sin, cos, ceil, log
from scipy.optimize import brenth
from time import perf_counter as perfc
from prettytable import PrettyTable
from numpy import arange
import matplotlib.pyplot as plt
'''
def f(x):
    return sin(x)

def fs(x):
    return -1*cos(x)

def fss(x):
    return -1*sin(x)
'''
def f(x):
    return sin(x)*(2**(x/10))

def fs(x):
    return 2**(x/10-2)*(10*cos(x)+log(2)*sin(x))

def fss(x):
    return (2**(x/10-3)*((log(2)*log(2)-100)*sin(x)+20*log(2)*cos(x)))/5

print('Вывод первой строки занял {:4.2g}s\n'.format(perfc()))

print('Уточнение корней методом brenth, функция y=sin(x)\n')
a, b = map(float, input('Задайте границы интервала: ').split())
eps_x = float(input('Укажите требуемую точность по X (>=0): '))
n = int(input('Введите число разбиений (0, если нужен шаг): '))
if n:
    h = (b-a)/n
else:
    h = float(input('Введите шаг (больше нуля): '))
    n = ceil((b-a+eps_x)/h)
max_iter = int(input('Задайте максимальное число итераций: '))
print('\n')


start_time = perfc()
x_points = []
x_points_fs = []
x_points_fss = []
table = PrettyTable(["№", "x1", "x2", "x", "f(x)", "error"])

# Нахождение нулей функции, а так же нулей двух её производных
for i in range(n):
    try:
        x_left = a+h*i
        x_right = a+h*(i+1)
        if x_right > b:
            x_right = b
        x = brenth(f, x_left, x_right, xtol= eps_x, maxiter= max_iter)
        x_points.append(x)
        table.add_row([i+1,"{: 5.5f}".format(x_left),"{: 5.5f}".\
            format(x_right),"{: 9.6f}".format(x),"{: 2.1g}".format(f(x)), 0])
    except ValueError:
        # Одинаковый знак
        #table.add_row([i+1, "{: 5.5f}".format(x_left), "{: 5.5f}".\
        #               format(x_right), "-", "-", 1])
        pass
    except RuntimeError:
        # Не сошлось за н итераций
        table.add_row([i+1, "{: 5.5f}".format(x_left), "{: 5.5f}".\
                       format(x_right), "-", "-", 2])
        pass
    
    try:
        x_points_fs.append(brenth(fs, (x_left), (x_right), xtol= eps_x,\
                                maxiter= 1000))
    except:
        pass
    
    try:
        x_points_fss.append(brenth(fss, (x_left), (x_right), xtol= eps_x,\
                                 maxiter= 1000))
    except:
        pass

print(table)
print("\n\nОбщее время вычислений и вывода - {:5.2g}с"\
      .format(perfc() - start_time))

# Вывод графика
#plt.xkcd(scale=1, length=100, randomness=3)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

x_graph = arange(a-eps_x, b+eps_x, abs(a-b)/300)
y_graph = [f(i) for i in x_graph]

plt.plot(x_graph, y_graph)

if len(x_points) > 0:
    # Точки зануления
    y_points = [f(i) for i in x_points]
    plt.plot(x_points, y_points, marker='x', ls='',\
             label='zero points', markersize=15, color='r')

if len(x_points_fs) > 0:
    # Точки экстремума
    y_points_fs = [f(i) for i in x_points_fs]
    plt.plot(x_points_fs, y_points_fs, marker='o', ls='',\
             label='extreme points', color='g')

if len(x_points_fss) > 0:
    # Точки перегиба
    y_points_fss = [f(i) for i in x_points_fss]
    plt.plot(x_points_fss, y_points_fss, marker='o', ls='',\
             label='bench points', color='y')

if len(x_points_fs) > 0:
    # Точки максимума и минимума
    plt.plot([x_points_fs[y_points_fs.index(max(y_points_fs))]],\
             [max(y_points_fs)], marker='v', ls='',\
             label='max point', color='c', markersize=9)
    plt.plot([x_points_fs[y_points_fs.index(min(y_points_fs))]],\
             [min(y_points_fs)], marker='^', ls='',\
             label='min point', color='m', markersize=9)
    
plt.legend(loc=0)
plt.xlim(a, b)
plt.ylim(-2, 2)
plt.show()

print("\nОбщее время работы программы - {:5.2g}с".format(perfc()))
