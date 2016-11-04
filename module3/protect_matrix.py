# Кириллов Алексей, ИУ7-12
# Защита(матрицы, №10): целочисленную матрицу Y(N,K) вывести по j элементов
# в строке(2<=j<=6), j<=K. Также печатать номера строк и столбцов.

N,K = map(int,input('Задайте размеры матрицы через пробел(N,K): ').split())
print('Введите матрицу построчно({:} строк, {:} столбцов):'.format(N,K))

Y = list()
for i in range(N):
    Y.append(list(map(int,input().split())))

j = int(input('Количество элементов в строке выводимой матрицы: '))
a = (K-1)//j+1    # Определяем число блоков вывода
print('Выводим матрицу в',a,'блок(-а,-ов):')

for k in range(a):   # По блокам

    if k>0: print('\n')
    
    # Вывод подписи столбцов
    print(' '*2,end='')
    for b in range(j*k,j*(k+1)):
        if b<K: print('{:2g}'.format(b+1),end=' ')
        
    print()
    
    for i in range(N):   # По стобцам
        
        for b in range(j*k,j*(k+1)):
            if b%j==0 and b<K: print(i+1,end=' ')
            if b<K: print('{:2g}'.format(Y[i][b]),end=' ')
            
        if i<(N-1): print()
