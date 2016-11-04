# Кириллов Алексей, ИУ7-12
# По координатам вершин треугольника на плоскости определить его стороны,
# биссектрису из наименьшего угла, является ли треугольник прямоугольным.
# По координатам точки определить её принадлежность треугольнику;
# если она лежит внутри, найти длину до дальней из сторон или её продолжения.

from math import sqrt

try:

    # Ввод координат вершин:
    print('Введите координаты вершин треугольника в формате "x y":')
    ax,ay = map(int,input('A: ').split())
    bx,by = map(int,input('В: ').split())
    cx,cy = map(int,input('С: ').split())
    dx,dy = map(int,input('Дополнительная точка: ').split())

except ValueError:
    print('Некорректный ввод! Разделяйте целые числа пробелами')

else:
    try:
        # Вычисление квадратов длин сторон:
        ab = (ax - bx)**2 + (ay - by)**2
        bc = (bx - cx)**2 + (by - cy)**2
        ca = (cx - ax)**2 + (cy - ay)**2

        # Проверка на прямоугольность треугольника:
        if ab== ca + bc or bc == ab + ca or ca == ab + bc:
            ort = 'прямоугольный'
        else:
            ort = 'не прямоугольный'
        
        # Нахождение длин сторон:
        ab = sqrt(ab)
        bc = sqrt(bc)
        ca = sqrt(ca)

        # Нахождение наименьшей стороны (напротив меньшего угла) и биссектрисы:
        if min(ab,bc,ca) == ab:
            biss = sqrt(bc*ca*(ab + bc + ca)*(bc + ca - ab))/(bc + ca)
        elif min(ab,bc,ca) == ca:
            biss = sqrt(ab*bc*(ab + bc + ca)*(ab + bc - ca))/(ab + bc)
        else:
            biss = sqrt(ab*ca*(ab + bc + ca)*(ab + ca - bc))/(ab + ca)

        # Нахождение коэффициентов прямых (сторон треугольника)
        Ac = (ay - by); Bc = (bx - ax); Cc = (ax*by - bx*ay)
        Ab = (cy - ay); Bb = (ax - cx); Cb = (cx*ay - ax*cy)
        Aa = (by - cy); Ba = (cx - bx); Ca = (bx*cy - cx*by)

        # Вывод всего, кроме операций над дополнительной точкой:
        print('\nРезультаты:\n')
        print('Длины сторон:')
        print('АВ = {:0.4f}, ВС = {:0.4f}, СА = {:0.4f}\n'.format(ab,bc,ca))
        print('Длина биссектрисы меньшего угла = {:0.4f}\n'.format(biss))
        print('Введённый треугольник - ',ort,'\n',sep='')
        
        # Проверка на принадлежность точки треугольнику:
        # Используется подстановка точки в уравнения прямых,
        # определяющих стороны треугольника
        if ((Aa*ax + Ba*ay + Ca)*(Aa*dx + Ba*dy + Ca)>=0 and
        (Ab*bx + Bb*by + Cb)*(Ab*dx + Bb*dy + Cb)>=0 and
        (Ac*cx + Bc*cy + Cc)*(Ac*dx + Bc*dy + Cc)>=0):

            # Нахождение расстояния до стороны:
            lentc = abs(Ac*dx + Bc*dy + Cc)/ab
            lentb = abs(Ab*dx + Bb*dy + Cb)/ca
            lenta = abs(Aa*dx + Ba*dy + Ca)/bc
            
            # Отбираем наиболее отдалённую сторону и выводим её:
            lent = max(lenta,lentb,lentc)

            print('Введённая точка внутри треугольника,')
            print('расстояние до дальней из сторон = {:0.4f}'.format(lent))

        else:

            print('Введённая точка не лежит в треугольнике.')
                  
    except ValueError:
        print('Ошибка значений')
