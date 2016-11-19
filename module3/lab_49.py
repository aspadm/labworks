# Кириллов Алексей, ИУ7-12
# Повернуть квадратную целочисленную матрицу F(N,N) по и против часовой стрелки
# без использования дополнительных массивов

#F = [[1,2,3],[8,9,4],[7,6,5]]
#F = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
#F = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]

try:
    #N = len(F)
    N = int(input('Задайте размер квадратной матрицы: '))
    n = N-1
    
    print('Введите',N,'строк с',N,'элементами, разделяя их пробелами:')
    F = []*N
    for i in range(N):
        F[i]=list(map(int,input().split()))

    print('Исходная матрица:')
    for i in range(N):
        for j in range(N):
            print('{:2g}'.format(F[i][j]),end=' ')
        print()
    
    # Против часовой:
    for i in range(N//2):
        for j in range(n-2*i):
            # 1 2
            # 4 3
            # 1)i+j,i 2)n-i,i+j 3)n-i-j,n-i 4)i,n-i-j
            # 1=2, 3=4, 1=3
            
            F[i+j][i],F[n-i][i+j] = F[n-i][i+j],F[i+j][i]
            F[n-i-j][n-i],F[i][n-i-j] = F[i][n-i-j],F[n-i-j][n-i]
            F[i+j][i],F[n-i-j][n-i] = F[n-i-j][n-i],F[i+j][i]

    print('Матрица после поворота против часовой стрелки:')
    for i in range(N):
        for j in range(N):
            print('{:2g}'.format(F[i][j]),end=' ')
        print()
    
    # По часовой:
    for i in range(N//2):
        for j in range(n-2*i):
            # 1 2
            # 4 3
            # 1)i+j,i 2)n-i,i+j 3)n-i-j,n-i 4)i,n-i-j
            # 1=4, 2=4, 1=3
            
            F[i+j][i],F[i][n-i-j] = F[i][n-i-j],F[i+j][i]
            F[n-i-j][n-i],F[n-i][i+j] = F[n-i][i+j],F[n-i-j][n-i]
            F[i+j][i],F[n-i-j][n-i] = F[n-i-j][n-i],F[i+j][i]

    print('Матрица после поворота по часовой стрелке(равна введённой):')
    for i in range(N):
        for j in range(N):
            print('{:2g}'.format(F[i][j]),end=' ')
        print()
            
except ValueError:
    print('Ошибка значений!')
#except IndexError:
    #print('Выход за пределы массива')
