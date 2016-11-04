# Кириллов, ИУ7-12, вариант 2

N = int(input('Задайте размер массива (число N): '))
t = float(input('Задайте коэффициент t: '))

A = list()
maxA = 0
otrA = -1
otr = vozr = ub = True

for i in range(N):
    
    A.append(((i + 1 - t)**2)/2 - 3)
    if A[i] > A[maxA] or i == 0:
        maxA = i
    if otr and A[i] <= 0:
        otr = False
        otrA = i
    if vozr and i>0:
        vozr = vozr and (A[i]>A[i-1])
    if ub and i>0:
        ub = ub and (A[i]<A[i-1])

if otr:
    print('\nНеотрицательная последовательность, ',end='')
else:
    print('\nМассив A до перестановки',end=' ')
    for i in range(N): print(A[i],end=' ')
    A[otrA],A[maxA] = A[maxA],A[otrA]
    print('\nПоследовательность - ',end='')
    
if vozr:
    print('возрастающая')
elif ub:
    print('убывающая')
else:
    print('общего вида')

    
print('\nИтоговый массив A',end=' ')
for i in range(N): print(A[i],end=' ')
