"""
NALOGA 3

Uporabnika vprašajte za 3 celoštevilske vrednosti in jih izpišite s pomočjo print() in type(). 
V eni vrstici preverite, ali je druga vrednost enaka prvi, in ali je tretja vrednost manjša ali enaka prvi.

"""

# Vnos števil in izpis
vrednost = []
for i in range(3):
    vrednost.append(input("Vnesi " + str(i+1) + ". vrednost: "))
for i in range(3):
    print("Vrednost " + str(i+1) + " je: " + str(vrednost[i]) + "    Tip: " + str(type(vrednost[i])))


# Preverjanje kriterija
if(vrednost[1] == vrednost[0] and vrednost[2] <= vrednost[0]):
    print("Druga vrednost je enaka prvi in tretja vrednost je manjša ali enka prvi.")
else:
    print("Vrednosti ne zadoščajo pogoju.")