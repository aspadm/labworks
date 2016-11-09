#Шибанова Дарья, ИУ7-12
#Вычислить сумму ряда с точностью до члена ряда < eps.
#В матрице определить элементы, большие суммы ряда, запомнить эти элементы
#в одномерном массиве.
#Поменять местами первый элемент массива и максимальный.
#Напечатать сумму ряда, матрицу и вектор.

#t - ряд
#Z - матрица
#X - вектор
a = float(input('Введите значение переменной, используемое \
для подсчёта ряда: '))
eps = 1e-5
Z = []
X = []
m = int(input('Введите число строк матрицы (не более 15): '))
n = int(input('Введите число столбцов матрицы (не более 10): '))
print('Введите значения каждой строки матрицы в строчку: ')
for i in range(m):
    Z.append([int(n) for n in input().split()])
print()
print('Матрица: \n')
for i in range(m):
    for j in range(n):
        print(Z[i][j],end=" ")
    print()
k = 0; t = t1 = a
while t>eps:
    k += 2
    t2 = t1*a*a/(k*k + k)
    if t2 <= eps:
        break
    else:
        t += t2
        t1 = t2
for i in range(m):
    for j in range(n):
        if Z[i][j] > t:
            X.append(Z[i][j])
x = len(X)
if x>0:
    print('Вектор X: ')
    for i in range(x):
        print(X[i],end=' ')
    print()
    xmax = X[0]
    nmax = 0
    for i in range(x):
        if X[i] > xmax:
            xmax = X[i]
            nmax = i
    if nmax != 0:
        X[0],X[nmax] = X[nmax],X[0]
    print('Вектор X с переставленными элементами: ')
    for i in range(x):
        print(X[i],end=' ')
else:
    print("\nЭлементы, больше суммы ряда, отсутствуют")
print("\n\nСумма ряда =",t)