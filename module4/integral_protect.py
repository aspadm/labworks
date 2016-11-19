# Кириллов Алексей, ИУ7-12
# Защита: написать процедуру вычисления интеграла методом 3/8 для одного
# заданного количества участков разбиения;

def f(x):
    return x*x

def int38(a,b,n):
    delta = b - a
    
    if n%3 != 0:
        return 'n не кратен 3, интеграл невычислим'

    I = f(a) + f(b)
    for i in range(1,n):
        y = f(a+i*delta/n)
        if i%3 == 0:
            y *= 2
        else:
            y *= 3
        I += y
        
    return I*3*delta/n/8


a,b,n = map(int,input('Введите a,b,n: ').split())
print(int38(a,b,n))
            
