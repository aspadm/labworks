# Кириллов, ИУ7-12, вариант 7

# В каждой строке матрицы G(m,n) (m<=10, n<=12) найти суммы элементов,
# расположенных до и после максимального в строке. Если сумму нельзя вычислить,
# то принять её за ноль.
# Вывести исходную матрицу, номер столбца максимального, найденные суммы.

m,n = map(int,input('Введите количество строк и столбцов: ').split())
print('Введите матрицу построчно:')
G = list()
M = list()
for i in range(m):
    G.append(list(map(int,input().split())))
    M.append(list([0]*3))

for i in range(m):
    M[i][0] = G[i][:].index(max(G[i][:]))+1

    for j in range(M[i][0]-1):
        M[i][1] += G[i][j]
    for j in range(M[i][0],n):
        M[i][2] += G[i][j]

print('Исходная матрица, номер максимального в строке и суммы: ')
for i in range(m):
    for j in range(n+3):
        if j<n:
            print(G[i][j],end=' ')
        else:
            print(M[i][j-n],end=' ')
    print()
