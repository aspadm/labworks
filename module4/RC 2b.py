# Кириллов, ИУ7-12
# Вариант 7

# Вывести, возможно ли составить строку A, используя все элементы строки R;
# выводить исходную строку и результат. Предусмотреть ввод нескольких строк A.

# Возможности языка использовать ЗАПРЕЩЕНО

def scount(string,letter):
    k = 0
    for i in range(len(string)):
        if string[i] == letter:
            k += 1
    return k

R = input('Введитое строку R: ')

while True:
    A = input('Введите подстроку A или оставьте пустой для выхода: ')
    
    if len(A) == 0:
        break
    
    yes = True
    
    for i in range(len(A)):
        if scount(A,A[i]) > scount(R,A[i]):
            yes = False
            break
    
    print('\nИз строки R = "',R,'" ',end='')
    if yes:
        print('МОЖНО',end='')
    else:
        print('НЕЛЬЗЯ',end='')
    print(' составить A = "',A,'"\n',sep='')
