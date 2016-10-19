# Кириллов Алексей, ИУ7-12

# Найти сумму ряда -1<x<1 с точностью Е

try:
    e = float(input('Введите требуемую точность: '))
    x = float(input('Введите коэффициент х: '))
    
    if -1>=x or x>=1:
        print('Некорректный х');
        raise ValueError
    
    z = x; s = 0; k = 0

    while z>e:
        k+=1
        z = x**(k*2-1)/(k*2+1)
        s += z
        #print('debug:',k,z,s)

    if k == 0: s = 2*x # Если не было входа в цикл 
    s = (s-z)*2

    print('\nСумма ряда с точностью {} равна {:0.8f}'.format(e,s))

except ValueError:
    print('Ошибка типов!')
