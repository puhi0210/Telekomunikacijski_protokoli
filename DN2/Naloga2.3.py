"""
Naloga 3
Iz danega dictionary-ja d izpišite vse ključe, katerih vrednost vsebuje črko r ali veliko tiskano črko R.
d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}
"""

d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}

# Izpis ključev
our_keys = list(d.keys())
print(our_keys)

our_keys_r = []

# Ločevanje ključev ki vsebujejo črko "r"
for i in range(len(our_keys)):
    if our_keys[i].lower().find("r") != -1:
        our_keys_r.append(our_keys[i])
        
print(our_keys_r)