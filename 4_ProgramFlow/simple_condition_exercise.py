# x = 5
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")

x = input("Enter a number ")
y = str(input(f"You entered {x}. Please enter another number "))

if x > y:
    print("{0} is greater than {1}".format(x, y))
elif x < y:
    print("{0} is smaller than {1}".format(x, y))
else:
    print("{0} equals {1}".format(x, y))
