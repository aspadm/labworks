# Кириллов Алексей, ИУ7-22
# Реализация однофайловой csv таблицы формата "адрес координаты". Команды:

menu = '''\
0 - выход
1 - создание новой базы
2 - добавление записи
3 - поиск по записи/её части
4 - вывод таблицы
'''

example_base = '''школа №1;1;1\nУЛК;2;2\nИзмайловский дворец;\
3;3\nм. Бауманская;4;4\n'''
base_name = 'example.csv'
base_open = False

def open_base():
    global base
    global base_name
    global base_open
    
    if not base_open:
        print('Нет открытой базы; открыть',base_name,'(y) или другую (n)?')
        if input() == 'n':
            base_name = input('Введите имя базы для открытия:')+'.csv'
        base = open(base_name,'a+')
        base_open = True
    else:
        print('Работа с базой',base_name)

choice = ''
while True:
    print(menu)
    choice = input('Введите номер выбранного пункта меню: ')
    print()

    if choice == '1':
        if base_open:
            base.close()
            base_open = False
        base_name = input('Введите имя новой базы (без расширения): ')+'.csv'
        base = open(base_name,'w')
        if input('Добавить в неё примеры записей? (y/n): ') == 'y':
            base.write(example_base)
        base.close()

    elif choice == '2':
        open_base()
        print('''\nВводите новые записи формата "объект широта долгота",
разделяя их переносом строки. Двойной перенос строки завершит ввод.
Использовать символ ";" запрещено.''')
        new_record = input()
        while new_record != '':
            new_record = new_record.rsplit(' ',2)
            new_record = new_record[0]+';'+new_record[1]+';'+new_record[2]+'\n'
            base.write(new_record)
            new_record = input()

    elif choice == '3':
        open_base()
        base.seek(0)
        seek_row = 4
        print('Выполнить поиск по всей базе(y) или по конкретному столбцу(n)?')
        if input() != 'y':
            print('''Выберите номер столбца:
0 - название объекта/строения
1 - широта
2 - долгота
''')
            seek_row = int(input())
        seek_full = False
        if seek_row != 4:
            print('Точное значение (y) или достаточно вхождения (n)?')
            if input() == 'y': seek_full = True
        phrase = input('Введите искомое значение: ')

        print('\nРезультаты поиска:')
        counter = 0
        for i in base.readlines():
            if seek_row != 4:
                record = i[:-1].split(';')[seek_row]
            else:
                record = i[:-1].replace(';',' ')
            if seek_full and phrase == record or\
            (not seek_full and phrase in record):
                print(i[:-1].replace(';','\t'))
                counter += 1
        print('\nНайдено записей:',counter)

    elif choice == '4':
        open_base()
        print('Объект',' '*12,'широта',' '*10,'долгота')
        base.seek(0)
        for i in base.readlines():
            print(i.replace(';','\t\t',2),end='')

    elif choice == '0':
        if base_open:
            base.close()
        print('Произведён выход')
        #exit(0)
        break

    else:
        print('Неверный выбор! Введите цифру от 0 до 4:')
        continue
    print('\n'+'='*77+'\n')

