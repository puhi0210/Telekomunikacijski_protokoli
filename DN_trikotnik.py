""" 
DOMAČA NALOGA
Ustvari funkcijo ki za parameter vzame velikost trikotnika.
Tega nato izriše s pomočjo print funkcije
"""
def trikotnik(velikost):
    for i  in range(1, velikost+1):
        print(" " * (velikost-i+1) + "*" * ((2*i)-1))

velikost = input("Podaj velikost željenega trikotnika: ")
print("Vaš trikotnik: \n")
trikotnik(int(velikost))