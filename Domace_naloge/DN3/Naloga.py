import json


with open('C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJE/Domace_naloge/DN3/DATA/zacetniData.json', 'r') as fz:
    zacetniData = json.load(fz)

with open('C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJE/Domace_naloge/DN3/DATA/updateData.json', 'r') as fu:
    updateData = json.load(fu)


zacetniSlovar = {x["name"]:x for x in zacetniData["persons"]}

print(zacetniSlovar)
print(zacetniData)

for oseba in updateData["persons"]:
    if oseba["name"] in zacetniSlovar.keys():
        zacetniSlovar[oseba["name"]].update(oseba)

print(zacetniSlovar)
print(zacetniData)

with open('C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJE/Domace_naloge/DN3/DATA/zacetniData.json', 'w') as f:
    json.dump(zacetniData, f, indent=2)