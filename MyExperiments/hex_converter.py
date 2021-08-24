choice = '-'
print("Please choose number to convert to hex "
      "or press 0 to exit: ")
while choice != 0:
    choice = int(input())
    print(hex(choice))
else:
    print("Bye")
