# Кириллов Алексей, ИУ7-12
# Сформировать массив размера 101, вывести его и новый - с вычеркнутым
# третьим отрицательным членом. В случае отсутствия 3х отрицательных,
# вывести сообщение.

from random import random

k = n = c = 0
A = list()

try:
    r = int(input('Размер исходного массива: '))

    # Автозаполнение
    #s,c = map(int,input('Коэффициент и сдвиг рандома: ').split())
    
    print('Исходный массив:')
    A = list(map(int,input().split()))
    
    for i in range(r):
        if c!=0:
            A.append(round(random()*s+c))
            print(A[i],end=' ')
        if A[i]>=0:
            continue
        elif k<3:
            k += 1
        if k==3:
            k +=1
            n = i
    print()

    if k<3:
        if k != 0:
            print('В массиве всего',k,'отрицательных чисел')
        else:
            print('В массиве нет отрицательных чисел')
    else:
        print('Полученный массив:')
        for i in range(r):
            if i==n:
                continue
            else:
                print(A[i],end=' ')

except ValueError:
    print('Ошибка значений!')
    
            
        
