# Кириллов Алексей, ИУ7-22
# Защита (текстовые БД)

base = open('ABC.txt','r')
s = base.read(1)
long = ''
predl = ''
n = -1
tek = 0
prev = True
thispred = False
glasn = ['a','A','e','E','y','Y','u','U','i','I','o','O']

while s != '':
    if s == '\n':
        s = base.read(1)
        continue
    if s == '.':
        for i in predl:
            if i in glasn:
                prev = False
                if tek >= n:
                    n = tek
                    thispred = True
                tek = 0
            else:
                prev = True
                tek += 1
                
        if thispred:
            thispred = False
            long = predl
        predl = ''
        
    else:                
        predl += s
    s = base.read(1)

print(long,n)
