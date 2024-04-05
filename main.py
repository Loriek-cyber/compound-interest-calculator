aaInterest = float(input("Inserisci il tuo tasso di interesse:"))
ddInterest = aaInterest/365
Invstart = float(input("Inserisci il tuo investimento iniziale:"))
durata = int(input("Inserisci la durata in anni:"))
mensile = int(input("inserisci una quantitò mensile:"))

def percente(a,b):
    return (a/100)*b

tot = Invstart

for n in range(0,durata):
    for n in range(0,12):
        for n in range(0,30):
            tot = tot + percente(tot,ddInterest)
        tot = tot+mensile
        

print("il totole è",tot)

