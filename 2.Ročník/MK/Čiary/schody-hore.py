import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

for i in range(5): #Pocet schodov
    canvas.create_line(10+i*50, 400-i*50, 10+i*50, 400-(i+1)*50)
    canvas.create_line(10+i*50, 400-(i+1)*50, 10+(i+1)*50, 400-(i+1)*50)

canvas.mainloop()