def prepocitaj():
    dlazdice = 40
    pocet_dlazdic = 1246
    nova_dlazdica = 30
    plocha_dlazdice = dlazdice*dlazdice
    nova_plocha_dlazdice = nova_dlazdica*nova_dlazdica
    pocet_novych_dlazdic = plocha_dlazdice*pocet_dlazdic/(nova_plocha_dlazdice)
    zaokruhleny_vysledok = round(pocet_novych_dlazdic, 2)
    return zaokruhleny_vysledok

vysledok = prepocitaj()

#Vela moznosti printu
print("Bude potrebných {} dlaždíc".format(vysledok))
print(f"Bude potrebných %s dlaždíc" % vysledok)
print("Bude potrebných " + str(vysledok) + " dlaždíc")
print(f"Bude potrebných {vysledok} dlaždíc")
