if 0:
    print("True")
else:
    print("False")

name = input("PLease enter you name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
