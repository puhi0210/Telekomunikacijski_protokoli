"""
NALOGA 2

Napišite program seštevalnik, ki sešteje dva list-a tako, da s for loop zanko iterirate po list-u. Seštevajte elemente po indexih in rezultate dodajte v novi list (uporabi .append).

List 1: [0,1,2,3,4,5,6,7,8,9]
List 2: [9,8,7,6,5,4,3,2,1,0]

Rezultat mora biti naslednji list: [9,9,9,9,9,9,9,9,9,9] 

"""

# Definiranje seznamov
list1 =  [0,1,2,3,4,5,6,7,8,9]
list2 =  [9,8,7,6,5,4,3,2,1,0]
listVsota =[]

# Seštevanje
for i in range(len(list1)):
    listVsota.append(list1[i]+list2[i])

print(listVsota)