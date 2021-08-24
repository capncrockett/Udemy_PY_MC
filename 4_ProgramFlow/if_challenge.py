name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age <= 30:
    print("{}, welcome to club 18-30.".format(name))
elif 900 == age:
    print("Yoda?")
else:
    print("I'm sorry {}, holidays are only for cool people, Weezer,"
          " and candid photography.".format(name))

print("-" * 30)

if 17 < age < 31:
    print("{}, welcome to club 18-30.".format(name))
elif 900 == age:
    print("Yoda?")
else:
    print("I'm sorry {}, holidays are only for cool people, Weezer,"
          " and candid photography.".format(name))
