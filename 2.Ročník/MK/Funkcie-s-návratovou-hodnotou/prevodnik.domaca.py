def na_palce(pocet):
    palce = pocet*0.3937
    return round(palce, 2)
def na_stopy(pocet):
    stopy = pocet*0.032
    return round(stopy, 2)
def na_yardy(pocet):
    yardy = pocet*0.0109
    return round(yardy, 2)

cm = 10

stopy = na_stopy(cm)
yardy = na_yardy(cm)
palce = na_palce(cm)

print(f"Dĺžka {cm} cm je:")
print(f"{stopy} stôp")
print(f"{yardy} yardov")
print(f"{palce} palcov")