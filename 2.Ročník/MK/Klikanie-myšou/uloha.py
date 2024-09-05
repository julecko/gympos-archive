import tkinter

canvas = tkinter.Canvas(width=1000, height=700, bg="brown") #Vyzera to na obrazku skor ako dark red
canvas.pack()

def clovek(x, y):
    #Telo
    canvas.create_line(x, y, x+15, y+55, x-15, y+55, x, y, width=5)
    #Hlava - Defaultne je veľkosť 1 ale tak, je to napísané špecifický v zadaní tak pre istotu som to zadal exaktne "width=1"
    canvas.create_oval(x+15, y, x-15, y-30, fill="white", width=1)
def jablko(x, y):
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="red", outline="red")
    canvas.create_line(x+3, y-20, x+7, y-35, x+15, y-35, x+3, y-20, width=3)
def kresli(suradnice):
    x = suradnice.x
    y = suradnice.y
    #Súradnice sú približné, dá sa to aj inými presnejšími funckiami ktoré však v dobe zadania domácej úlohy neboli známe
    if 125 <= x <= 425 and 150 <= y <= 450:
        jablko(x, y)
    else:
        clovek(x, y)
#Strom
canvas.create_rectangle(250, 700, 300, 400, fill="black")
canvas.create_oval(75, 500, 475, 100, fill="green")


canvas.bind("<ButtonPress-1>", kresli)

canvas.mainloop()