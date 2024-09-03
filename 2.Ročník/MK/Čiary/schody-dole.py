import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

for i in range(5): #Pocet schodov
    canvas.create_line(i*50, 10+i*50, (i+1)*50, 10+i*50)
    canvas.create_line((i+1)*50, 10+i*50, (i+1)*50, 10+(i+1)*50)

canvas.mainloop()