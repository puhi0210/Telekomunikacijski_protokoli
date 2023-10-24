"""
Naloga 4
Poiščite vsa praštevila med 1 in 50.

"""

# Funkcija, ki vzame za parameter število, za katerega želimo izvedeti če je praštevilo. Če je praštevilo, vrne 1, če ne pa 0
def jePrastevilo(a):
    p = 1    
    for i in range(2, int((a/2)+1)): # Izračunamo ostanek pri deljenju podanega števila z vsakim številom do polovice podanega (časovna kompleksnost)
        if (a % i) == 0: # Računanje ostanka pri deljenju
            p = 0
    return p
 

# Funkcija, vzame za parameter število, do katerega želimo poiskati vsa praštevila. Vrne list praštevil do podanega števila
def prastevila(input):
    out = []
    for n in range(2, input+1): # Pregleda vsako število posebej
        if(jePrastevilo(n)): # Če je število praštevilo, ga doda na list
            out.append(n)
    return out

print(prastevila(50))
