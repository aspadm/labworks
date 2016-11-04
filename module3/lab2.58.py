# Кириллов Алексей, ИУ7-12
# Определить, упорядоченна ли по неубыванию последовательность размера М [2,35]

try:
    a = f = 0
    up = True
    M = int(input('Задайте размер последовательности(М): '))

    s = input()
    #s = s + ' '
    k = ''
    
    """for i in range(len(s)):
        if s[i] != ' ':
            k += s[i]
            print(k)
        else:
            b = a
            a = int(k)
            k = ''
            if a<b and f>0:
                up = False
                break
            f += 1"""
    for k in s.split():
        b = a
        a = int(k)
        if f == 0:
            f = 1
            continue
        if a<b and f>0:
            up = False
            break
            
    print('Последовательность',end=' ')
    if up:
        print('упорядочена',end='')
    else:
        print('НЕ упорядочена',end='')
    print(' по неубыванию')
    
except TypeError:
    print('Ошибка типов!')

except ValueError:
    print('Невозможно преобразовать\'',k,'\'в число',sep='')
