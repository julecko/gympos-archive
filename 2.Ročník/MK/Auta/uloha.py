import tkinter

canvas = tkinter.Canvas(width=1700, height=1000, bg="white")
canvas.pack()

def auto_a(x, y): #Suradnice pravy horny roh auta
    canvas.create_rectangle(x, y, x+250, y+45, fill="red") #Konstrukcia
    canvas.create_rectangle(x, y, x+20, y+15, fill="yellow") #Zadne svetlo

    #Horna konstrukcia
    canvas.create_line(x+50, y, x+80, y-40)
    canvas.create_line(x+80, y-40, x+190, y-40)
    canvas.create_line(x+190, y-40, x+210, y)

    #Antena
    canvas.create_line(x+160, y-40, x+175, y-60)
    canvas.create_oval(x+173, y-58, x+177, y-62, fill="blue") #Gulka priemer 4pixely

    #Okno
    canvas.create_rectangle(x+90, y, x+160, y-40, fill="blue")

    #Gula na dverach
    canvas.create_oval(x+90, y+8, x+98, y+16, fill="black")

    #Lave Koleso
    canvas.create_oval(x+35, y+25, x+85, y+75, fill="white")
    canvas.create_oval(x+50, y+40, x+70, y+60, fill="black")
    #Prave Koleso
    canvas.create_oval(x+160, y+25, x+210, y+75, fill="white")
    canvas.create_oval(x+175, y+40, x+195, y+60, fill="black")
def auto_b(x, y):
    #Prve idu kolesa z dovodu toho, ze ich kontrukcia prekryva a teda musia ist prve inak by oni
    #prekryli konstrukciu

    #Lave koleso
    canvas.create_oval(x+60, y+70, x+100, y+110, fill="grey")
    canvas.create_oval(x+70, y+80, x+90, y+100, fill="black")

    #Prave koleso
    canvas.create_oval(x+150, y+70, x+190, y+110, fill="grey")
    canvas.create_oval(x+160, y+80, x+180, y+100, fill="black")

    #Konstrukcia
    canvas.create_rectangle(x, y, x+260, y+80, fill="red")
    canvas.create_rectangle(x+60, y, x+170, y-65, fill="red")
    
    #Predne svetlo
    canvas.create_rectangle(x+260, y, x+245, y+15, fill="yellow")

    #Okna
    canvas.create_rectangle(x+64, y, x+110, y-60, fill="light blue")
    canvas.create_rectangle(x+120, y, x+165, y-60, fill="light blue")

    #Typek
    canvas.create_line(x+145, y, x+145, y-25, width=5)
    #Ohnuta ruka, da sa urobit aj napriamo
    canvas.create_line(x+145, y-25, x+155, y-15, width=5)
    canvas.create_line(x+155, y-15, x+165, y-15, width=5)

    canvas.create_oval(x+133, y-47, x+157, y-23, fill="brown")
def auto_c(x, y):
    #Konstrukcia
    canvas.create_rectangle(x, y, x+200, y+50, fill="red")
    canvas.create_rectangle(x+40, y, x+160, y-70, fill="blue")

    #Svetla
    canvas.create_rectangle(x, y, x+10, y+10, fill="yellow")
    canvas.create_rectangle(x+200, y, x+190, y+10, fill="yellow")

    #Tie ciary co tam su 💀
    canvas.create_line(x+40, y, x+40, y+50, fill="grey")
    canvas.create_line(x+100, y-70, x+100, y+50, fill="grey")
    canvas.create_line(x+160, y, x+160, y+50, fill="grey")

    #Odtahovacia gula/dzindzik zpredu
    canvas.create_rectangle(x+200, y+35, x+220, y+45, fill="grey")

    #Lave koleso
    canvas.create_oval(x+30, y+50, x+70, y+90, fill="black")
    canvas.create_oval(x+35, y+55, x+65, y+85, fill="grey")

    #Prave koleso
    canvas.create_oval(x+140, y+50, x+180, y+90, fill="black")
    canvas.create_oval(x+145, y+55, x+175, y+85, fill="grey")
def auto_d(x, y):
    #Konstrukcia
    canvas.create_rectangle(x, y, x+200, y+120, fill="red", outline="red")
    canvas.create_rectangle(x+200, y+20, x+255, y+120, fill="black")

    #Okno
    canvas.create_rectangle(x+230, y+35, x+250, y+70, fill="blue")

    #Lave koleso
    canvas.create_oval(x+20, y+105, x+60, y+145, fill="black")
    canvas.create_oval(x+30, y+115, x+50, y+135, fill="white")

    #Prave koleso
    canvas.create_oval(x+150, y+105, x+190, y+145, fill="black")
    canvas.create_oval(x+160, y+115, x+180, y+135, fill="white")
def auto_e(x, y):
    #Konstrukcia
    canvas.create_rectangle(x, y, x+200, y+100, fill="red", outline="red")
    canvas.create_oval(x-50, y-50, x+50, y+50, fill="white", outline="white")
    canvas.create_oval(x+150, y-50, x+250, y+50, fill="white", outline="white")

    #Okno
    canvas.create_rectangle(x+60, y+5, x+140, y+50, fill="blue")

    #Svetla
    canvas.create_rectangle(x, y+50, x+10, y+80, fill="yellow")
    canvas.create_rectangle(x+200, y+50, x+185, y+65, fill="yellow")

    #Lave koleso
    canvas.create_oval(x+25, y+85, x+65, y+125, fill="white", outline="white")
    canvas.create_oval(x+28, y+88, x+62, y+122, fill="black")
    canvas.create_oval(x+31, y+91, x+59, y+119, fill="white")
    canvas.create_oval(x+37, y+97, x+53, y+113, fill="black")

    #Prave koleso
    canvas.create_oval(x+135, y+85, x+175, y+125, fill="white", outline="white")
    canvas.create_oval(x+138, y+88, x+172, y+122, fill="black")
    canvas.create_oval(x+141, y+91, x+169, y+119, fill="white")
    canvas.create_oval(x+147, y+97, x+163, y+113, fill="black")

#Prikladove zavolanie v loope
for i in range(3):
    auto_e(50+i*550, 100)
    auto_d(330+i*520, 80)

canvas.mainloop()