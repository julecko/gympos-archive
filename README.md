# ✨ Gympos Archív ✨
## Úvod
Tento archív bol založený na pomoc ostatným v ťiaži, keď potrebujú pomoc so školskými úlohami alebo len chcú mať viac času pre seba. Aktuálne archív obsahuj úlohy z informatiky ale pevne verím, že s dostatočnou aktivitou a pomocou ostatných by sa mohol rozšíriť na viaceré predmety. To je avšak hudba budúcnosti a nateraz je len informatika. V prípade, že aktualne riešenia na úlohy nepomôže, stačí napísať sťažnosť/pripomienku. Síce je v archíve málo úloh, netreba sa obávať, časom ich bude pribudať.
## Implementácia
Z dôvodu, že python kód v tomto priečinku je licensovaný a akákoľvek kopirácia je striktne zakázaná, stále avšak existujú možnosti ako ho použiť a privlastniť

Príklad č.1
```python
import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

for i in range(10):
    canvas.create_line(10, 10+i*10, 200, 10+i*10)

canvas.mainloop()
```
Na použitie daného kódu je potrebné urobiť pár úprav ako napríklad upraviť hodnoty v príkazoch, počty loopov(opakovaní), pridať medery, zmeniť názvy premnných, zmeniť názvy funckií/procedúr atď...
Z kódu hore by upravená verzia vyzerala nejak takto
```python
import tkinter

canvas = tkinter.Canvas(width = 550, height = 450)
canvas.pack()

for i in range(8):
    canvas.create_line(35, 15+i*12, 180, 15+i*12)

canvas.mainloop()
```
Ako môžeme vidieť, bolo upravených viacero hodnôt, počty opakovania, menené nové riadky a zároveň pridané medzery pri definovaní canvy.

Viac exemplárných príkladov bude pridaných v budúcnosti.
