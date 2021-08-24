quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
# Use a for loop and an if statement to print just the capitals in the quote above.

separators = ""
for char in quote:
    if char.isupper():
        separators = separators + char
print(separators)

print("*" * 30)

for char in quote:
    if char.isupper():
        print(char)

print("*" * 30)

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

print("*" * 30)

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        separators = separators + char
print(separators)
