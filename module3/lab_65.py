# Кириллов Алексей, ИУ7-12
# Сформировать вектор из ненулевых элементов целочисленной матрицы,
# проходя по столбцам. В полученном векторе заменить третий отрицательный
# элемент суммой всех предыдущих, если это возможно.

try:
    R = Z = list()
    s = k = n = 0
    a,b = map(int,input('Задайте размеры матрицы(стлбц стрк): ').split())
    Z = [[0]*a]*b
    print('Введите {:} строк по {:} значений:'.format(b,a))
    
    for i in range(b):
        Z[i]=list(map(int,input().split()))

    for j in range(a):
        for i in range(b):
            if Z[i][j]<0:
                k += 1
                if k == 3:
                    n = Z[i][j]
            if k<3:
                s += Z[i][j]
            if Z[i][j] != 0:
                R.append(Z[i][j])

    if k >= 3:
        print('Вектор до замены элемента на',s,':')
        for i in range(len(R)):
            print(R[i],end=' ')
        R[R.index(n)]=s
        print()
    elif k == 0:
        print('Вектор не содержит отрицательных элементов')
    else:
        print('Вектор содержит',k,'отрицательный(х) элемент(а)')

    print('Исходная матрица:')
    for i in range(b):
        for j in range(a):
            print(Z[i][j],end=' ')
        print()

    print('Полученный вектор:')
    for i in range(len(R)):
        print(R[i],end=' ')           
 
    
except ValueError:
    print('Некорректное значение!')
