# Кириллов Алексей, ИУ7-22
# Защита сортировки, метод перемешивания (шейкер)

arr = list(map(float, input('Массив для сортировки: ').split()))

b = len(arr)-1
a = 0
up = True
steps = 0
swaps = 0

while b-a>0:
    end = True
    if up:
        i = a
        while i < b:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                k = i
                end = False
                swaps += 1
            else:
                i += 1
        if not end:
            b = k
    else:
        i = b
        while i > a:
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                k = i
                end = False
                swaps += 1
            else:
                i -= 1
        if not end:
            a = k
    up = not up
    steps += 1
    if end:
        break

print('\nОтсортированный массив:')
for i in arr:
    print(i, end=' ')

print('\n\nПроходов:', steps)
print('Обменов:', swaps)
