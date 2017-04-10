# Кириллов Алексей, ИУ7-22
# Сортировка слиянием

from numpy import array, sort
#from random import randint
from random import random
from time import perf_counter as perfc
from math import sqrt, ceil

def bmark():
    return perfc()*1000

def randint(b):
    return ceil(random()*b)

def example_sorted(n):
    return [x for x in range(n)]

def example_back_sorted(n):
    return [x for x in range(n-1, -1, -1)]

def example_random(n, b):
    arr = []
    for i in range(n):
        arr.append(randint(b))
    return arr

def example_big_intersections(n):
    return example_random(n, ceil(sqrt(n)))

def example_small_intersections(n):
    return example_random(n, n**2)

def test_sort(arr):
    b = array(arr)
    a = bmark()
    c = sort(b, kind="mergesort")
    #print(c)
    return bmark()-a

result = []

for i in range(7):
    n = 10**i
    print('Размер выборки:', n)
    testarr = example_sorted(n)
    print('Наилучший  случай: ', test_sort(testarr))
    testarr = example_back_sorted(n)
    print('Наихудший  случай: ', test_sort(testarr))
    testarr = example_big_intersections(n)
    print('Частые пересечения:', test_sort(testarr))
    testarr = example_small_intersections(n)
    print('Редкие пересечения:', test_sort(testarr))
