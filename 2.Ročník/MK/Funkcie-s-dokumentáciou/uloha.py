def JUNIOR(minuty):
    vm = 30
    cena_mesiac = 5
    cena_minuta = 0.59
    if minuty <= vm:
        return cena_mesiac
    else:
        return cena_mesiac + (minuty-vm)*cena_minuta
def STUDENT(minuty):
    vm = 75
    cena_mesiac = 10
    cena_minuta = 0.49
    if minuty <= vm:
        return cena_mesiac
    else:
        return cena_mesiac + (minuty-vm)*cena_minuta
def EFEKT(minuty):
    vm = 100
    cena_mesiac = 20
    cena_minuta = 0.45
    if minuty <= vm:
        return cena_mesiac
    else:
        return cena_mesiac + (minuty-vm)*cena_minuta
def SENIOR(minuty):
    vm = 30
    cena_mesiac = 7.50 #Moze sa aj upravit na 7.5, je to jedno
    cena_minuta = 0.19
    if minuty <= vm:
        return cena_mesiac
    else:
        return cena_mesiac + (minuty-vm)*cena_minuta

minuty = int(input("Prevolane minúty: "))
typ = input("Typ programu: ")

if typ == "JUNIOR":
    vyska_platby = JUNIOR(minuty)
elif typ == "STUDENT":
    vyska_platby = STUDENT(minuty)
elif typ == "EFEKT":
    vyska_platby = EFEKT(minuty)
elif typ == "SENIOR":
    vyska_platby = SENIOR(minuty)
#Tento else je cisto optional zalezitost
else:
    print("Nespravny typ")
    vyska_platby = 0

print(f"Pre {minuty} prevolaných minút v programe {typ} musíte zaplatiť {vyska_platby}")