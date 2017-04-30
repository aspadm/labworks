# Кириллов Алексей, ИУ7-22
from math import sqrt
from tkinter import *
root = Tk()
draw_pole = Canvas(root, width = 800, height = 600, bg = "white")

def dist(x, y, x1, y1, x2, y2):
    lenth = abs((x-x1) * (y2-y1) - (y-y1) * (x2-x1)) /\
    sqrt((x2-x1)**2 + (y2-y1)**2)
    #print(lenth)
    return lenth

def uline(a1, b1, a2, b2, b):
    if b1 == b2:
        return 0
    else:
        return (a2 - a1)*(b - b1)/(b2 - b1) + a1

R = float(input("Задайте радиус окружностей: "))

points = []
print("\nВведите x и y точки через пробел; пустая строка завершает ввод:")
s = input()
while s != "":
    points.append(list(map(float, s.split())))
    s = input()

circles = []
print("Введите x и y центра окружности через пробел; \
пустая строка завершает ввод:")
s = input()
while s != "":
    circles.append(list(map(float, s.split())))
    s = input()

max_k = 0
point_a = 0
point_b = 0

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        k = 0
        a = 0
        b = 0
        c = 0
        for circle in circles:
            if dist(circle[0], circle[1],
                    points[i][0], points[i][1],
                    points[j][0], points[j][1]) < R:
                k += 1
        if k > max_k:
            point_a = i
            point_b = j
            max_k = k

print("{:} пересечений с окружностями у линии, проходящей\nчерез точки \
({:}; {:}) и ({:}; {:})".format(max_k, points[point_a][0], points[point_a][1],
                                       points[point_b][0], points[point_b][1]))

min_x = max_x = points[0][0]
min_y = max_y = points[0][1]

for point in points:
    max_x = max(max_x, point[0])
    min_x = min(min_x, point[0])
    max_y = max(max_y, point[1])
    min_y = min(min_y, point[1])

for circle in circles:
    max_x = max(max_x, circle[0])
    min_x = min(min_x, circle[0])
    max_y = max(max_y, circle[1])
    min_y = min(min_y, circle[1])

scale = min(500/(max_y - min_y), 700/(max_x - min_x))
disp_x = 50 + round((700 - (max_x - min_x)*scale)/2)
disp_y = 550 - round((500 - (max_y - min_y)*scale)/2)

x = round(disp_x - min_x*scale)
y = round(disp_y + min_y*scale)
draw_pole.create_line(0, y, 800, y, width=2, fill="grey", arrow=LAST)
draw_pole.create_line(x, 600, x, 0, width=2, fill="grey", arrow=LAST)

draw_pole.create_text(x + 8, 9, text = "y",\
          font="Arial 8", justify=CENTER, fill="green")
draw_pole.create_text(790, y - 9, text = "x",\
          font="Arial 8", justify=CENTER, fill="green")

x1 = uline(points[point_a][0], points[point_a][1],
    points[point_b][0], points[point_b][1], (max_y-min_y)*2)
x2 = uline(points[point_a][0], points[point_a][1],
    points[point_b][0], points[point_b][1], -(max_y-min_y)*2)
y1 = uline(points[point_a][1], points[point_a][0],
    points[point_b][0], points[point_b][1], x1)
y2 = uline(points[point_a][1], points[point_a][0],
    points[point_b][0], points[point_b][1], x2)

x1 = round(disp_x + (x1 - min_x)*scale)
y1 = round(disp_y - (y1 - min_y)*scale)
x2 = round(disp_x + (x2 - min_x)*scale)
y2 = round(disp_y - (y2 - min_y)*scale)
draw_pole.create_line(x1, y1, x2, y2, width=2, fill="magenta")

R = round(R * scale)

for point in points:
    x = round(disp_x + (point[0] - min_x)*scale)
    y = round(disp_y - (point[1] - min_y)*scale)
    draw_pole.create_oval(x-2, y-2, x+2, y+2, fill="black")
    draw_pole.create_text(x, y - 13,text="({:};{:})".format(point[0], point[1]),\
          font="Arial 8", justify=CENTER, fill="blue")

for circle in circles:
    x = round(disp_x + (circle[0] - min_x)*scale)
    y = round(disp_y - (circle[1] - min_y)*scale)
    draw_pole.create_oval(x - R, y - R, x + R, y + R, outline = "red")
    draw_pole.create_oval(x - 1, y - 1, x + 1, y + 1, fill = "red")
    draw_pole.create_text(x, y - 13, text="({:};{:})".format(circle[0],\
                          circle[1]), font="Arial 8", justify=CENTER, \
                          fill="green")

draw_pole.pack()
root.mainloop()
