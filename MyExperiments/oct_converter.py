choice = '-'
print("Please choose number to convert to oct "
      "or press 0 to exit: ")
while choice != 0:
    choice = int(input())
    print(oct(choice))
else:
    print("Bye")
