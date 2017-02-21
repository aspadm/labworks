# Кириллов Алексей, ИУ7-22
# Реализация однофайловой csv таблицы формата "адрес координаты". Команды:

# Пункты меню
menu = '''\
0 - выход
1 - создание новой базы
2 - добавление записи
3 - поиск по записи/её части
4 - вывод таблицы
'''

# Пример записей
example_base = '''\
школа №21;1;1
УЛК (МГТУ);2;2
Измайловский дворец;3;3
м. Бауманская;4;4
'''

base_open = False # Открыта ли база в настоящий момент
base_name = 'example.csv' # Имя файла базы

# Проверка на наличие открытой базы/само открытие
def open_base():
    global base # Непосредственно база
    global base_name
    global base_open
    # Если база не открыта, предложить открыть последнее использованное имя
    if not base_open:
        print('Нет открытой базы; открыть',base_name,'(y) или другую (n)?')
        # Или введённое пользователем
        if input() == 'n':
            base_name = input('Введите имя базы для открытия:')+'.csv'
        base = open(base_name,'a+')
        base_open = True
    # Если открыта, то вывести её имя
    else:
        print('Работа с базой',base_name,'\n')

choice = '' # Выбранный пункт меню
while True:
    print(menu)
    choice = input('Введите номер выбранного пункта меню: ')
    print()

    if choice == '1': # Создание новой базы
        if base_open: # Закрываем открытую, при её наличии
            base.close()
            base_open = False
        base_name = input('Введите имя новой базы (без расширения): ')+'.csv'
        base = open(base_name,'w')
        if input('Добавить в неё примеры записей? (y/n): ') == 'y':
            base.write(example_base)
        base.close()

    elif choice == '2': # обавление записей в базу
        open_base() # Проверка на наличие открытой базы/само открытие
        print('''\nВводите новые записи формата "объект широта долгота",
разделяя их переносом строки. Двойной перенос строки завершит ввод.
Использовать символ ";" запрещено.''')
        new_record = input()
        while new_record != '':
            new_record = new_record.rsplit(' ',2) # Разбиение записи на три столбца
            # Форматирование для хранения базы в .csv формате
            new_record = new_record[0]+';'+new_record[1]+';'+new_record[2]+'\n'
            base.write(new_record)
            new_record = input()

    elif choice == '3': # Реализация поиска
        open_base() # Проверка на наличие открытой базы/само открытие
        base.seek(0) # Перевод курсора в начало базы
        seek_row = 3 # указатель на тип поиска: 4 - по записи,
        # 0-2 - по соответственным столбцам
        print('Выполнить поиск по всей базе(y) или по конкретному столбцу(n)?')
        if input() != 'y':
            print('''Выберите номер столбца:
0 - название объекта/строения
1 - широта
2 - долгота
''')
            seek_row = int(input())
        seek_full = False # Искать ли полное соответствие или просто вхождение
        if seek_row != 3:
            print('Точное значение (y) или достаточно вхождения (n)?')
            if input() == 'y': seek_full = True
        phrase = input('Введите искомое значение: ')
        print('\nРезультаты поиска:')
        
        # Подключение файла для хранения результатов
        search_out = open('search.txt','w')
        search_out.write('Поиск в '+['имени объекта',\
                                    'широте','долготе','записи'][seek_row]+' ')
        search_out.write('точного значения' if seek_full else 'вхождения')
        search_out.write(' значения "'+phrase+'":\n\n')

        counter = 0 # Количество найденных записей
        while True:
            i = base.readline()
            if i == '': break # Проверка на EOF
            # "Вытаскивание" из записи данных для поиска
            if seek_row != 3:
                record = i[:-1].split(';')[seek_row]
            else:
                record = i[:-1].replace(';',' ')
            # Непосредственно поиск
            if seek_full and phrase == record or\
            (not seek_full and phrase in record):
                search_out.write(i)
                print(i[:-1].replace(';','\t'))
                counter += 1
        search_out.write('\nНайдено записей: '+str(counter))
        print('\nНайдено записей:',counter)
        search_out.close()

    elif choice == '4': # Вывод базы на экран
        open_base() # Проверка на наличие открытой базы/само открытие
        print('Объект',' '*16,'широта',' '*8,'долгота')
        base.seek(0)
        while True:
            rec = base.readline()
            if rec == '': break
            rec = rec.split(';')
            print(rec[0].ljust(23),rec[1].ljust(15),rec[2],end='')

                
    elif choice == '0': # Выход
        if base_open:
            base.close()
        print('Произведён выход')
        #exit(0)
        break

    else: # Обработка некорректного ввода номера меню
        print('Неверный выбор! Введите цифру от 0 до 4:')
        continue
    print('\n'+'='*77+'\n')

