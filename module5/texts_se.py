# Кириллов Алексей, ИУ7-12
# Вариант №24
# Текст задан массивом строк; найти: самое длинное слово в каждой строке,
# количество слов во всём тексте/в последних двух строках,
# наиболее часто встречающееся слово.
# Заменить арифметическое действие (+,-) на результат.
# Выравнивать строки по ширине (число пробелов между словами строки отличается
# на 1 или меньше).
# Добавить замену одного слова другим во всём тексте; удалить из первых трёх
# строк заданное слово.

# Версия БЕЗ использования возможностей языка

text =  """Сегодня +15 градусов
            тепла
            и это -
            ложь.
            Вот.
            Так вот."""

def splitl(s):
    k = []
    z = ''
    for i in range(len(s)):
        if s[i]!='\n':
            z += s[i]
        else:
            k.append(z)
            z = ''
    k.append(z)
    return k

def splits(s):
    k = []
    z = ''
    for i in range(len(s)):
        if s[i]!=' ':
            z += s[i]
        elif len(z):
            k.append(z)
            z = ''
    k.append(z)
    return k

def dz(s):
    if s[-1]==',' or s[-1]=='.':
        s = s[:-1]
    return s

def summ(s):
    k = list()
    for i in range(len(s)):
        k += s[i]
    return k

def calc(s):
    if len(s) <= 1: # Если дефис/пустая строка
        return s
    
    if '+' in s or '-' in s:
        digits = ''
        expr = [1]
        if s[0] == '-':
            s = s[1:]
            expr[0] = -1
            
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-':
                digits += ' '
                expr.append(1 if s[i] == '+' else -1)
            else:
                digits += s[i]
        try:
            digits = list(map(int,digits.split()))
        except ValueError:
            return s
        if len(digits) == len(expr):
            x = 0
            for i in range(len(digits)):
                x += digits[i]*expr[i]
            s = str(x)

    return s

def lenm(s,a = 0,b = 0):
    if b == 0:
        b = len(s)-1
    k = 0
    for i in range(a,b+1):
        k += len(s[i])
    return k

def printm(s,lab=''):
    print(lab)
    for i in range(len(s)):
        for j in range(len(s[i])):
            print(s[i][j],end=' ')
        print()
    print()

def printv(s,lab=''):
    print(lab)
    for i in range(len(s)):
        print(dz(s[i]))
    print()
        
def printh(s,n=0):
    p = list()    # Длина строки
    z = list()    # Новые пробелы
    for i in range(len(s)):    # Находим длины строк
        p.append(len(summ(s[i])))
    k = max(p)
    if n < k+len(s[p.index(k)])-1:    # Задаём ширину вывода
        n = k+len(s[p.index(k)])-1
    for i in range(len(s)):
        a = n - p[i]    # Находим число пробелов
        b = len(s[i])    # Число слов
        if b > 1:
            z.append([' '*(a//(b-1))]*(b-1))    # Минимальное число пробелов
            z[i].append('')
            for j in range(a - a//(b-1)*(b-1)):
                z[i][j%(b-2)] += ' '    # Дополняем текст по ширине
        else:
            z.append([' '*a])
            
    for i in range(len(s)):
        for j in range(len(s[i])):
            if len(s[i]) == 1:
                print(z[i][j]+s[i][j],end='')
            else:
                print(s[i][j]+z[i][j],end='')
        print()
    print()

def printr(s):
    p = list()    # Длина строки
    for i in range(len(s)):    # Находим длины строк
        p.append(len(summ(s[i])))
    k = max(p)
    for i in range(len(s)):
        print(' '*(k-p[i]-len(s[i])+1+len(s[p.index(k)])),end='')
        for j in range(len(s[i])):
            print(s[i][j],end=' ')
        print()
    print()

# Ввод текста
if input('Вводить текст заново? (д/н)<н>: ') == 'д':
    print('Введите текст построчно; пустая строка прервёт ввод')
    text = list()
    while True:
        s = list(input().split())
        if len(s) > 0:
            text.append(s)
        else:
            break
else:
    text = splitl(text)
    for i in range(len(text)):
       text[i] = splits(text[i]) 

printm(text,'Заданный текст:')
print('С выравниванием по ширине:')
printh(text,0)

print('С выравниванием по правому краю:')
printr(text)

wcount = lenm(text)    # Количество слов в тексте

lwords = [0]*len(text)

lwc3es = 0
lwc3es = lenm(text,len(text)-2)    # Количество слов в последних 3х строках

for i in range(len(text)):
    for j in range(len(text[i])):
        if len(dz(text[i][j])) > len(dz(text[i][lwords[i]])):
            lwords[i] = j

for i in range(len(text)):
    lwords[i] = text[i][lwords[i]]

texta = summ(text)
cword = 0

for i in range(wcount):
    if texta.count(texta[i]) > texta.count(texta[cword]):
        cword = i
        
cword = texta[cword]

printv(lwords,'Самые длинные слова по строкам:')

for i in range(len(text)):
    for j in range(len(text[i])):
        text[i][j] = calc(text[i][j])

print('Всего слов:',wcount)
print('Слов в последних 2х строках:',lwc3es)
print('Наиболее частое слово:',cword)

print('\nС выполненной заменой математических выражений:')
printh(text)

zam = list()
zam.append(input('Заменить слово '))
zam.append(input('словом '))

for i in range(len(text)):
    for j in range(len(text[i])):
        if (dz(text[i][j])) == (zam[0]):
            if text[i][j][-1]==',' or text[i][j][-1]=='.':
                text[i][j] = zam[1]+text[i][j][-1]
            else:
                text[i][j] = zam[1]

print('\nС выполненной заменой:')
printh(text)

ud = input('Удалить из первых 3х строк слово ')

for i in range(3):
    while ud in text[i]:
        text[i].remove(ud)
    while ud+'.' in text[i]:
        text[i][text[i].index(ud+'.')] = text[i][text[i].index(ud+'.')][-1]
    while ud+',' in text[i]:
        text[i][text[i].index(ud+',')] = text[i][text[i].index(ud+',')][-1]
        
print('\nИтоговый текст:')   
printh(text)
