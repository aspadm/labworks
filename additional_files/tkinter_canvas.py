# Пример графического модуля
from tkinter import *
root=Tk()

canv = Canvas(root,width=500,height=500,bg="lightblue", cursor="pencil")  # создание холста

canv.create_line(200,50,300,50,width=3,fill="blue")
canv.create_line(0,0,100,100,width=2,arrow=LAST)   # Линия

x = 75
y = 110

canv.create_rectangle(x,y,x+80,y+50,fill="white",outline="blue") # Прямоугольник

canv.create_polygon([250,100],[200,150],[300,150],fill="yellow") # Многоугольник

canv.create_polygon([250,100],[200,150],[300,150],fill="yellow")
canv.create_polygon([300,80],[400,80],[450,75],[450,200],
          [300,180],[330,160],outline="white",smooth=1)

canv.create_oval([20,200],[150,300],fill="gray50")      # Эллипс
canv.create_arc([160,230],[230,330],start=0,extent=140,fill="lightgreen")
canv.create_arc([250,230],[320,330],start=0,extent=140, style=CHORD,fill="green")
canv.create_arc([340,230],[410,330],start=0,extent=140, style=ARC,outline="darkgreen",width=2)

canv.create_text(20,330,text="Опыты с графическими примитивами\nна холсте",  # Текст
          font="Verdana 12",anchor="w",justify=CENTER,fill="red")
x=10
while x < 450:
     canv.create_rectangle(x,400,x+50,450)  
     x = x + 60 

canv.pack()
root.mainloop()
