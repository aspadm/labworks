# Инициализация холста
from tkinter import *
root = Tk()
draw_pole = Canvas(root, width = 640, height = 480, bg = "white")

# Изначально заданный массив точек
points = [[0, 1],
          [1, 2],
          [-3, -1],
          [2, 2],
          [0, 0],
          [-2, 1]]
lenths = []

# Определение расстояния между точками
def line(xy1, xy2):
    x1 = xy1[0]
    y1 = xy1[1]
    x2 = xy2[0]
    y2 = xy2[1]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# Расскоментировать для ввода точек вручную
"""
points = []
print("Input point's x y:")
s = input()
while s != "":
    points.append(list(map(float, s.split())))
    s = input()
"""    

print("Точки:")
for point in points:
    print("({:}; {:})".format(point[0], point[1]))

# Подсчёт расстояния от точки до остальных
for i in range(len(points)):
    lenths.append(0.0)
    for j in range(len(points)):
        lenths[i] += line(points[i], points[j])

central_index = lenths.index(min(lenths))
central_point = points[central_index]
central_radius = lenths[central_index]/(len(lenths)-1)

print("\nНаименьшая длина до остальных у точки ({:}; {:}),".format(\
    central_point[0], central_point[1]),"среднее расстояние - {:2.2f}".format(\
    central_radius))

# Нахождение размера окна вывода в пунктах (координатах графика)
min_x = max_x = points[0][0]
min_y = max_y = points[0][1]

for point in points:
    if point[0] > max_x:
        max_x = point[0]
    elif point[0] < min_x:
        min_x = point[0]
    if point[1] > max_y:
        max_y = point[1]
    elif point[1] < min_y:
        min_y = point[1]

# Определение смещений и коэффициента растяжения (количества пикселей в пункте)
screen_scale = min(460/(max_y - min_y), 620/(max_x - min_x))
offset_x = 10 + round((620 - (max_x - min_x)*screen_scale)/2)
offset_y = 470 - round((460 - (max_y - min_y)*screen_scale)/2)
central_radius *= screen_scale

x = round(offset_x - min_x*screen_scale)
y = round(offset_y + min_y*screen_scale)

# Отрисовка осей и подписей к ним
draw_pole.create_line(0, y, 640, y, width=2, fill="grey", arrow=LAST)
draw_pole.create_line(x, 480, x, 0, width=2, fill="grey", arrow=LAST)

draw_pole.create_text(x + 8, 9, text = "y",\
          font="Verdana 8", justify=CENTER, fill="green")
draw_pole.create_text(635, y - 9, text = "x",\
          font="Verdana 8", justify=CENTER, fill="green")

# Вывод точек и их координат
for point in points:
    x = round(offset_x + (point[0] - min_x)*screen_scale)
    y = round(offset_y - (point[1] - min_y)*screen_scale)
    point.append(x)
    point.append(y)
    #print(x, y)
    draw_pole.create_oval(x-2, y-2, x+2, y+2, fill="black")
    draw_pole.create_text(x, y - 9,text="{:};{:}".format(point[0], point[1]),\
          font="Verdana 6", justify=CENTER,fill="blue")

# Вывод центральной точки и радиуса среднего расстояния
draw_pole.create_oval(round(points[central_index][2] - central_radius),\
                      round(points[central_index][3] - central_radius),\
                      round(points[central_index][2] + central_radius),\
                      round(points[central_index][3] + central_radius),\
                      fill = "", outline = "#FF0000")

draw_pole.create_oval(points[central_index][2] - 4,\
                      points[central_index][3] - 4,\
                      points[central_index][2] + 4,\
                      points[central_index][3] + 4, fill = "green")

# Упаковка холста и отображение на экране
draw_pole.pack()
root.mainloop()
