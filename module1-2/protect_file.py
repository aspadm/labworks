# Кириллов Алексей, ИУ7-12
# Защита(файлы)
# Удалить из файла все повторные вхождения строк

example = '''\
это - строка
и даже
это - строка
мне
весело повторять
что
мне
весело повторять
это
интересно
писать
код
писать
это
'''

if input('1 - создать пример, 0 - убрать повторы из файла: ')=='1':
    # Создание базы с примером
    file = open('testfile.txt','w')
    file.write(example)
    file.close()
    print(example)

else:
    base = [] # Массив уникальных строк по порядку
    file = open('testfile.txt','r')

    s = file.readline()
    while s != '':
        if s not in base:
            base.append(s)
        s = file.readline()
    file.close()

    file = open('testfile.txt','w')
    for s in base:
        file.write(s)
        print(s,end='')
    file.close()
