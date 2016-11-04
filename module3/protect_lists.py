# Кириллов Алексей, ИУ7-12
# Защита(Списки): Задан целочисленный массив A(N), 1<=N<=40, в котором
# все элементы разные. Выбрать случайным образом K(1<=K<=N) элементов
# этого массива без повторов.

from random import random

try:
    N = int(input('Задайте размер исходного массива: '))
    print('Задайте',N,'элементa(-ов) массива через пробел:')
    A = list(map(int,input().split()))
    K = int(input('Количество элементов новой выборки: '))
    C = set()
    B = list()
    
    while len(C)<K:
        y = A[round(random()*(N-1))]
        if not(C.__contains__(y)):
            C.add(y)
            B.append(y)
        
    print('\nПолученный массив: ')
    
    for i in range(K):
        print(B[i],end=' ')

except ValueError:
    print('Некорректный ввод!')
