# Take user input
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
numbers = user_input.split(",")

# Convert the tokens into integers
int_numbers = []
for digits in numbers:
    int_numbers.append(int(digits))

# Calculate the result a + b - c
a, b, c = int_numbers
result = a + b - c
# result = int_numbers[0] + int_numbers[1] + int_numbers[2]

# Output the result
print("user_input = {}".format(user_input))
print("numbers = {}".format(numbers))
print("int_numbers = {}".format(int_numbers))
print("a = {}".format(a))
print("b = {}".format(b))
print("c = {}".format(c))
print(result)
