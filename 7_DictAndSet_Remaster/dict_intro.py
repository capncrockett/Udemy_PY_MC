vehicles = {'dream': 'Honda 250T',
            # 'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250',
            'tenere': 'Yamaha XT650',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4',
            'roadster': 'Triumph Street Triple',
            # "starfighter": "Lockheed F-104",
            # "learjet": "Bombardier Learjet 75",
            # "toy": "Glider",
            # "virago": "Yamaha XV535"
    }


vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# Upgrade the Virago
vehicles["virago"] = 'Yamaha XV535'

del vehicles["starfighter"]

# This doesn't exists so cause an error
# del vehicles["f1"]

# Better way to check if a key exists.
result = vehicles.pop("f1", f"f1?! {None} You wish! Sell the LearJet and you might afford a racing car")
print(result)

# plane = vehicles.pop("learjet")
# print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()


# Not an efficient way to work with Dicts
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

# .items() is the better way.
for key, value in vehicles.items():
    print(key, value, sep=", ")
