""" 
NALOGA 1

Uporabnika zaprosite, naj vnese neko celo število. 
To vrednost shranite v spremenljivko z imenom n in jo izpišite ter izpišite njen tip. 
Nato to vrednost pretvorite v float vrednost. Dobljeno float vrednost shranite v spremenljivko n. Nato n izpišite in izpišite njen tip.

"""

# Vnos števila in sprememba vnosa v int
n = input("\nVnesite celo število: ")
n = int(n)
print("\nŠtevilo tipa int: " + str(n) + "    Tip: " + str(type(n))) 
# Sprememba v float
n = float(n)
print("\nŠtevilo tipa float: " + str(n) + "    Tip: " + str(type(n)) +"\n") 