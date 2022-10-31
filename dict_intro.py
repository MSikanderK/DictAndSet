vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

#upgrade virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish!")
print(result)
plane = vehicles.pop("learjet")
print(plane)
bike = vehicles.pop("tenere", "not present")
print(bike)
print()


# print("Key   Vehicle")
# for key in vehicles:
#     print("{:12}:   {}".format(key, vehicles[key]))
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

for key, value in vehicles.items():
    print(key, value, sep=", ")
