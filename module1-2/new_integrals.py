# Кириллов Алексей, ИУ7-22
# Работа с интегралами из меню

def f(x):
    return x*x

def parabola(a,b,n): 
    s = 0 
    h = (b-a)/n 
    for i in range(n): 
        s += f(a+i*h) + 4 * f(a+i*h+h/2) + f(a+i*h+h) 
    s *= h/6
    return s

def Integral(a,b,n=0,e=1):
    if not n:
        n = 1
        while abs(parabola(a,b,n)-parabola(a,b,n+1)) > e:
            n += 1
        print('\nЧисло разбиений =',n)
    S = parabola(a,b,n)
    return S

menu = 1
while menu:
    print('Выберите действие:\n')
    print('\t1 - подсчитать интеграл с заданной точностью')
    print('\t2 - подсчитать интеграл с заданным числом разбиений')
    print('\n\t0 - выход\n')

    menu = int(input('Введите номер действия: '))
    if menu:
        a,b = map(int,input('\n\nЗадайте границы интервала: ').split())
    if menu == 1:
        e = float(input('Введите требуемую точность: '))
        S = Integral(a,b,0,e)
    if menu == 2:
        n = int(input('Задайте число разбиений: '))
        S = Integral(a,b,n)
    if menu:
        print('\nИнтеграл функции y = x*x на отрезке [',a,',',b,'] =',S,'\n\n')
