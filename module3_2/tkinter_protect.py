# Шибанова Дарья, ИУ7-22
# Защита по tkinter

from math import sqrt
from tkinter import *
root = Tk()
draw_pole = Canvas(root, width = 640, height = 480, bg = "white")

point = []
r = 0

def input_point():
  global point
  global r
  n = int(input('Введите количество окружностей: '))
  for i in range(n):
    print('Введите координаты ',i,' центра',end = ' ')
    x,y = map(int,input().split())
    point.append((x,y))
  r = float(input('Введите радиус окружностей: '))
    
def len_line(a,b):
  x = a[0] - b[0];
  y = a[1] - b[1];
  return sqrt(x*x+y*y)

def find_imax(point,r):
  max = 0
  i_max = -1
  for i in range(len(point)):
    count = -1;
    for j in range(len(point)):
      if len_line(point[i],point[j]) <= 2*r:
        count += 1
    if count > max:
      i_max = i
      max = count
  return i_max;

input_point()

i_max = find_imax(point,r)

print('Максимальное персечение у оружности с центром  в ', point[i_max])

min_x = max_x = point[0][0]
min_y = max_y = point[0][1]

for pt in point:
    max_x = max(pt[0], max_x)
    min_x = min(pt[0], min_x)
    max_y = max(pt[1], max_y)
    min_y = min(pt[1], min_y)

max_x += r
max_y += r
min_x -= r
min_y -= r

screen_scale = min(460/(max_y - min_y), 620/(max_x - min_x))
offset_x = 10 + round((620 - (max_x - min_x)*screen_scale)/2)
offset_y = 470 - round((460 - (max_y - min_y)*screen_scale)/2)
r *= screen_scale

x = round(offset_x - min_x*screen_scale)
y = round(offset_y + min_y*screen_scale)

draw_pole.create_line(0, y, 640, y, width=2, fill="grey", arrow=LAST)
draw_pole.create_line(x, 480, x, 0, width=2, fill="grey", arrow=LAST)

draw_pole.create_text(x + 8, 9, text = "y",\
          font="Verdana 8", justify=CENTER, fill="green")
draw_pole.create_text(635, y - 9, text = "x",\
          font="Verdana 8", justify=CENTER, fill="green")

for i in range(len(point)):
    pt = point[i]
    x = round(offset_x + (pt[0] - min_x)*screen_scale)
    y = round(offset_y - (pt[1] - min_y)*screen_scale)

    draw_pole.create_oval(x-2, y-2, x+2, y+2, fill="black")
    draw_pole.create_text(x, y - 9,text="{:};{:}".format(pt[0], pt[1]),\
          font="Verdana 6", justify=CENTER,fill="blue")
    clr = "#FF0000" if i == i_max else "#00FF00"
    draw_pole.create_oval(round(x - r),\
                          round(y - r),\
                          round(x + r),\
                          round(y + r),\
                          fill = "", outline = clr)

draw_pole.pack()
root.mainloop()
