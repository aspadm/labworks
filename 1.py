# Кириллов Алексей, ИУ7-12
# Защита лабораторной "Определение св-в треугольника"
# Для заданной координатами точки, лежащей в треугольнике, найти расстояние
# до ближайшей стороны.

from math import sqrt

try:
    ax,ay,bx,by,cx,cy = map(float,input('Введите координаты вершин:').split())
    dx,dy = map(float,input('Введите координаты точки внутри:').split())

    # Коэффициенты прямой:
    # A = y1 - y2; B = x2 - x1; C = x1y2 - x2y1;
    # Нахождение расстояния до стороны:
    # |A*x + B*y + C|/a, где a - длина стороны
    # Длина стороны:
    # sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # Нахождение расстояний до всех сторон:
    # Для точки d, сторона ab
    lenthc=abs((ay-by)*dx+(bx-ax)*dy+ax*by-bx*ay)/(sqrt((ax-bx)**2+(ay-by)**2))
    # Аналогично для двух других:
    lenthb=abs((ay-cy)*dx+(cx-ax)*dy+ax*cy-cx*ay)/(sqrt((ax-cx)**2+(ay-cy)**2))
    lentha=abs((cy-by)*dx+(bx-cx)*dy+cx*by-bx*cy)/(sqrt((cx-bx)**2+(cy-by)**2))

    # Выбираем минимальное:
    lenth = min(lentha, lenthb, lenthc)

    print('Расстояние от точки до ближайшей стороны = {:0.4f}'.format(lenth))

except ValueError:
    print('Неверный ввод!')
    
except ZeroDivisionError:
    print('Треугольник вырожден')
