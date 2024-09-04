import tkinter

canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()

def srdiecko(x, y):
    canvas.create_line(x, y+50, x-40, y-20, width=5)
    canvas.create_line(x, y+50, x+40, y-20, width=5)

    canvas.create_line(x+40, y-20, x+20, y-40, width=5)
    canvas.create_line(x-40, y-20, x-20, y-40, width=5)

    canvas.create_line(x+20, y-40, x, y-20, width=5)
    canvas.create_line(x-20, y-40, x, y-20, width=5)
def x(x, y):
    canvas.create_line(x-40, y-40, x+40, y+40, width=5)
    canvas.create_line(x+40, y-40, x-40, y+40, width=5)
def v(x, y):
    canvas.create_line(x, y, x-50, y-40, width=5)
    canvas.create_line(x, y, x+50, y-40, width=5)

    canvas.create_line(x, y-10, x-25, y-30, width=5)
    canvas.create_line(x, y-10, x+25, y-30, width=5)

def stvorce(x, y):
    canvas.create_line(x-70, y, x-30, y-40, width=5)
    canvas.create_line(x-70, y, x-30, y+40, width=5)

    canvas.create_line(x-30, y-40, x+10, y, width=5)
    canvas.create_line(x-30, y+40, x+10, y, width=5)


    canvas.create_line(x-10, y, x+30, y-40, width=5)
    canvas.create_line(x-10, y, x+30, y+40, width=5)

    canvas.create_line(x+30, y-40, x+70, y, width=5)
    canvas.create_line(x+30, y+40, x+70, y, width=5)

#Domcek
canvas.create_rectangle(100, 300, 700, 700, fill="brown")
canvas.create_polygon(100, 300, 700, 300, 400, 50, fill="grey")

for i in range(4):
    stvorce(175+i*150, 375)
for i in range(4):
    srdiecko(175+i*150, 500)
for i in range(4):
    v(175+i*150, 650)

canvas.mainloop()