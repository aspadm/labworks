# Кириллов Алексей, ИУ7-12
# Вариант №24
# Текст задан массивом строк; найти: самое длинное слово в каждой строке,
# количество слов во всём тексте/в последних двух предложениях,
# наиболее часто встречающееся слово.
# Заменить арифметическое действие (+,-) на результат.
# Выравнивать строки по ширине (число пробелов между словами строки отличается
# на 1 или меньше).
# Добавить замену одного слова другим во всём тексте; удалить из первых трёх
# трок заданное слово.

# Версия с использованием ЛЮБЫХ возможностей языка

text = [['Данный', 'текст', 'является', 'тестовой', 'заглушкой'],
        ['и', 'не', 'несёт', 'никакого', 'смысла','15-7+16+386-199'],
        ['Здесь', 'абсолютно', 'точно', 'отсутствует', 'что-то', 'полезное'],
        ['лучше', 'съешь', 'ещё', 'этих', 'французских', 'булок'],
        ['да', 'выпей', 'чаю', 'с', 'лимоном'],
        ['ещё', 'одна', 'строка', 'текста'],
        ['и','ещё','-','мало','ли','кому-то', 'это', 'интересно', 'читать'],
        ['держите', 'ещё', 'одну','2+2']]

def summ(s):
    k = list()
    for i in range(len(s)):
        k += s[i]
    return k

def calc(s):
    if '+' in s or '-' in s:
        digits = ''
        expr = [1]

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

def printh(s,n=0):
    p = list()
    z = list()
    for i in range(len(s)):
        p.append(len(summ(s[i])))
    k = max(p)
    if n < k+len(s[p.index(k)])-2:
        n = k+len(s[p.index(k)])-2
    for i in range(len(s)):
        a = n - p[i]
        b = len(s[i])
        z.append([' '*(a//b)]*len(s[i]))
    #for 
    for i in range(len(s)):
        if i>0: print()
        for j in range(len(s[i])):
            print(s[i][j]+z[i][j],end='')
    return 0

# Ввод текста
"""
print('Введите текст построчно; пустая строка прервёт ввод')
text = list()
while True:
    s = list(input().split())
    if len(s) >0:
        text.append(s)
    else:
        break
"""

wcount = lenm(text)    # Количество слов в тексте

lwords = [0]*len(text)

lwc3es = 0
lwc3es = lenm(text,len(text)-3)    # Количество слов в последних 3х строках

printm(text)
printh(text,50)
for i in range(len(text)):
    for j in range(len(text[i])):
        if len(text[i][j]) > len(text[i][lwords[i]]):
            lwords[i] = j
        #text[i][j] = calc(text[i][j])

for i in range(len(text)):
    lwords[i] = text[i][lwords[i]]
print()

texta = summ(text)
cword = 0

for i in range(wcount):
    if texta.count(texta[i]) > texta.count(texta[cword]):
        cword = i
        
cword = texta[cword]

print(lwords)
print(wcount)
print(lwc3es)
print(cword)
