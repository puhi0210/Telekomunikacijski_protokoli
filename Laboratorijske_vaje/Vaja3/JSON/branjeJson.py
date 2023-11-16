import json

with open("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/person.json", "r") as f:
    deserialized_person = json.load(f)

deserialized_person["age"] = 40
deserialized_person["married"] = False

print(deserialized_person)

with open("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/person.json", "w") as f:
    json.dump(deserialized_person, f, indent=4, sort_keys=False)