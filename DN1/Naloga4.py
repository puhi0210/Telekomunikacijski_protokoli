"""
NALOGA 4

Napišite funkcijo izpisi_trikotnik, ki sprejme celo število visina, ki predstavlja višino trikotnika. Funkcija naj vrne izpis trikotnika zvezdic v naslednji obliki:

Primer:

Če je visina enaka 5, naj funkcija izpiše:

*
**
***
****
*****

"""
# Funkcija ki izriše trikotnik
def izpisi_trikotnik(visina):
    for i  in range(1, visina+1):
        print("*" * (i))

# Vnos višine trikotnika
visina = int(input("\nPodaj višino željenega trikotnika: "))

# Izris rezultata
if(visina >= 0):
    print("\nVaš trikotnik: \n")
    izpisi_trikotnik(visina)
else:
    print("\nNeveljaven vnos!\n")