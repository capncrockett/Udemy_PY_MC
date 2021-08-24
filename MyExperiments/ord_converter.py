choice = '-'
print("Please choose one character to convert to ord. "
      "Press 0 to exit: ")
while choice != 0:
    choice = input()
    print(ord(choice))
    # Returns an integer representing the
    # Unicode code point of that character.
else:
    print("Bye")
