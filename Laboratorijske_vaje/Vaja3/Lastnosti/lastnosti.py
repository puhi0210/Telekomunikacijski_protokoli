import os
import json
from person_pb2 import Person

# Velikosti
file_size = os.path.getsize("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/POMOC/person.pb")
print(f"PB file size: {file_size} bytes")

file_size = os.path.getsize("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/POMOC/person.json")
print(f"JSON file size: {file_size} bytes\n")


# File type
with open("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/POMOC/person.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {type(value)}")





person_pb = Person()

with open('C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/POMOC/person.pb', 'rb') as f:
    person_pb.ParseFromString(f.read())


for field, value in person_pb.ListFields():
    print(f"Field: {field.name}, Type: {field.type}, Value: {value}")
