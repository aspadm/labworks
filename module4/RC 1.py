# Кириллов, ИУ7-12
# Вариант 3

# Перезаписать целочисленный массив D(J) (J<=9) элементами этого массива,
# стречающимися только один раз. Доп. массивы/множества не использовать.

D = list(map(int,input('Введите исходный массив: ').split()))
k = 0

while k<len(D):
    f = D[k]
    if D.count(f) == 1:
        k += 1
    else:
        for i in range(D.count(f)):
            D.remove(f)

if len(D) == 0:
    print('Все элементы повторяющиеся')
else:
    print('Массив чисел, входящих один раз:')
    for i in range(len(D)):
        print(D[i],end=' ')
