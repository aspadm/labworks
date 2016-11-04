# Кириллов Алексей, ИУ7-12
# Приложение: демонстрация некорректной работы escape последовательностей

print('Перевод строки')
print('aaa',end='')
print('\n',end='')
print('bbb')

print('Возврат каретки')
print('aaa',end='')
print('\r',end='')
print('bbb')

print('Звуковой сигнал')
print('aaa',end='')
print('\a',end='')
print('bbb')

print('Возврат на позицию влево')
print('aaa',end='')
print('\b',end='')
print('bbb')

print('Перевод страницы')
print('aaa',end='')
print('\f',end='')
print('bbb')

print('Нулевой разделитель')
print('aaa',end='')
print('\0',end='')
print('bbb')
