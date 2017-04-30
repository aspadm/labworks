# Кириллов Алексей, защита TkInter

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

def vline(x, y, x1, y1, x2, y2):
    return (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
'''
points = []
print("Введите x и y точки через пробел; пустая строка завершает ввод:")
s = input()
while s != "":
    points.append(list(map(float, s.split())))
    s = input()

triangles = []
print("Введите 3 пары x и y вершин треугольника через пробел;\n\
пустая строка завершает ввод:")
s = input()
while s != "":
    triangles.append(list(map(float, s.split())))
    s = input()
'''

points = [[0, 0],
          [1, 1],
          [-1, 2]]
triangles = [[3, 1, 4, 3, 1, 2],
             [0, 1, 1, 0, 6, 5],
             [-4, 0, -1, 4, -1, -2]]

max_k = 0
ind_k = (0, 0)
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        k = 0
        for triangle in triangles:
            z = [0, 0, 0]
            z[0] = vline(triangle[0], triangle[1], points[i][0], points[i][1],
                     points[j][0], points[j][1])
            z[1] = vline(triangle[2], triangle[3], points[i][0], points[i][1],
                     points[j][0], points[j][1])
            z[2] = vline(triangle[4], triangle[5], points[i][0], points[i][1],
                     points[j][0], points[j][1])
            #print(i,j,z)
            if (z[0]*z[1] <= 0) or (z[1]*z[2] <= 0) or (z[0]*z[2] <= 0):
                k += 1
        if k >= max_k:
            max_k = k
            ind_k = i, j

#print(ind_k,max_k)
print("{:} пересечений линии через точки ({:}; {:}) и ({:}; {:})".format(\
    max_k, points[ind_k[0]][0], points[ind_k[0]][1],
    points[ind_k[1]][0], points[ind_k[1]][1]))

min_x = max_x = points[0][0]
min_y = max_y = points[0][1]

for point in points:
    max_x = max(max_x, point[0])
    min_x = min(min_x, point[0])
    max_y = max(max_y, point[1])
    min_y = min(min_y, point[1])

for triangle in triangles:
    max_x = max(max_x, triangle[0], triangle[2], triangle[4])
    min_x = min(min_x, triangle[0], triangle[2], triangle[4])
    max_y = max(max_y, triangle[1], triangle[3], triangle[5])
    min_y = min(min_y, triangle[1], triangle[3], triangle[5])

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

x1 = uline(points[ind_k[0]][0], points[ind_k[0]][1],
    points[ind_k[1]][0], points[ind_k[1]][1], (max_y-min_y)*2)
x2 = uline(points[ind_k[0]][0], points[ind_k[0]][1],
    points[ind_k[1]][0], points[ind_k[1]][1], -(max_y-min_y)*2)
y1 = uline(points[ind_k[0]][1], points[ind_k[0]][0],
    points[ind_k[1]][0], points[ind_k[1]][1], x1)
y2 = uline(points[ind_k[0]][1], points[ind_k[0]][0],
    points[ind_k[1]][0], points[ind_k[1]][1], x2)

x1 = round(disp_x + (x1 - min_x)*scale)
y1 = round(disp_y - (y1 - min_y)*scale)
x2 = round(disp_x + (x2 - min_x)*scale)
y2 = round(disp_y - (y2 - min_y)*scale)
draw_pole.create_line(x1, y1, x2, y2, width=2, fill="magenta")

for triangle in triangles:
    dr = []
    for i in range(3):
        x = round(disp_x + (triangle[i*2] - min_x)*scale)
        y = round(disp_y - (triangle[i*2+1] - min_y)*scale)
        dr.append(x)
        dr.append(y)
    draw_pole.create_line(dr[0], dr[1], dr[2], dr[3], width=2, fill="cyan")
    draw_pole.create_line(dr[4], dr[5], dr[2], dr[3], width=2, fill="cyan")
    draw_pole.create_line(dr[0], dr[1], dr[4], dr[5], width=2, fill="cyan")
    for i in range(3):
        draw_pole.create_oval(dr[i*2]-2, dr[i*2+1]-2, dr[i*2]+2, dr[i*2+1]+2,
                              fill="red")
        draw_pole.create_text(dr[i*2], dr[i*2+1] - 13,text="({:};{:})".format(
            triangle[0], triangle[1]), font="Arial 8", justify=CENTER,
                              fill="green")

for point in points:
    x = round(disp_x + (point[0] - min_x)*scale)
    y = round(disp_y - (point[1] - min_y)*scale)
    draw_pole.create_oval(x-2, y-2, x+2, y+2, fill="black")
    draw_pole.create_text(x, y - 13,text="({:};{:})".format(point[0],
                                                            point[1]),\
          font="Arial 8", justify=CENTER, fill="blue")


draw_pole.pack()
root.mainloop()
