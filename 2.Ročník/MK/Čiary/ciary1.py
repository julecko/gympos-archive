import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

for i in range(10):
    canvas.create_line(10, 10+i*10, 200, 10+i*10)

canvas.mainloop()