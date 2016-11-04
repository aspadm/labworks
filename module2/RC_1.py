# Кириллов, ИУ7-12, вариант 15

L = int(input('Задайте размер массива (от 1 до 10): '))
print('Задайте элементы массива: ')
R = NUM = list()
maxR = 0

for i in range(L):
    
    R.append(int(input('R[{}] = '.format(i))))
    if R[i] > maxR or i == 0: maxR = R[i]

print('\nИсходный массив R',end=' ')
for i in range(L): print(R[i],end=' ')

R.append(maxR)

i = L
while True:
    if R.index(maxR) >= i:
        break
    else:
        NUM.append(R.index(maxR)+L+1-i)
        R.remove(maxR)
        i -= 1

print('\nПолученный массив NUM',end=' ')
for k in range(i+1,L+1): print(NUM[k],end=' ')

if i == 0:
    print('\nВсе элементы одинаковые')
else:
    print('\nСжатый массив R',end=' ')
    for k in range(i): print(R[k],end=' ')
