"""
Naloga 2
Iz sledečega lista our_list odstranite vrednost, ki se nahaja na indexu 4. 
Vrednost dodajte v dictionary pod ključ d. 
Nato iz dictionary our_dict pridobite vse vrednosti. 
Te vrednosti shranite v nov tuple in novonastali tuple primerjajte ali je enak podanemu tuple-u our_tuple.

our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

"""

our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

# Odstranjevanje vrednosti iz our_list in spreminjanje our_dict
our_dict["d"] = our_list.pop(4)

print(our_list)
print(our_dict)
 
# Zapisovanje vrednosti our_dict v novi tuple
new_tuple = tuple(our_dict.values())

# Primerjava tuple-ov
print("\nPrimerjava:")
print(new_tuple)
print(our_tuple)

if new_tuple == our_tuple:
    print("Tuple-a sta enaka")
else:
    print("Tuple-a nista enaka")
