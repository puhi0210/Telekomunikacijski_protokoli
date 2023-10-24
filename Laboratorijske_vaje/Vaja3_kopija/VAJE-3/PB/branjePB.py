import person_pb2

# Create an empty Person object
person = person_pb2.Person()

# Deserialize from file
with open("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/person.pb", "rb") as f:
    person.ParseFromString(f.read())

# Manipulate the data (e.g., change age and married status)
person.age = 31
person.married = False

# Serialize back to file
with open("C:/Users/Mihael Zeme/Documents/Sola/TelekomunikacijskiProtokoli/Vaje/VAJA-3/VAJE/VAJE-3/DATA/person_updated.pb", "wb") as f:
    f.write(person.SerializeToString())

# Print person object
print(person)