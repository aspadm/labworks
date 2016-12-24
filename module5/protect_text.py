# Кириллов Алексей, ИУ7-12
# Защита (текст)

# Найти предложения, в которых все слова состоят из чередующихся
# согласных и гласных букв.

sogl = 'бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
sogl = list(sogl[:])
gl = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
gl = list(gl[:])
razd = '.?!'
razd = list(razd[:])
#print(gl,sogl,razd)

def splitp(s):
    k = []
    z = ''
    for i in s:
        if i in razd:
            z += i
            k.append(z)
            z = ''
        else:
            z += i
    return k

def isCh(s):
    if len(s) == 0:
        return True
    flag = (s[0] in sogl)
    for i in s:
        if (i not in gl) and (i not in sogl):
            continue
        if i in gl and flag:
            return False
        if i in sogl and not flag:
            return False
        flag = not flag
    return True

def printbw(s,n):
    k = 0
    for i in s.split():
        k += len(i)
        if k >= n or len(i)>n:
            k = 0
            print()
        print(i,end = ' ')
    print()

text = 'Ракета пролетела. А я сижу на парте. Инжу надо закрыть.\
 А сколько у меня баллов по теоринфе? Много! Или мало? Давайте подпишем ещё \
 строчку - так интереснее! Ну хорошо, эту покажу. Напишу-ка я ещё.'

print('Исходный текст:')
printbw(text,60)
    
text = list(splitp(text))

print('\nРазбитый по предложениям:')
for i in text:
    print(i.lstrip())

v = []
print('\nПредложения, в которых все слова из чередующихся согл/гл букв:')
for i in text:
    flag = True
    for j in i.split():
        flag *= isCh(j)
    if flag:
        v.append(i.lstrip())

for i in v:
    printbw(i,60)


