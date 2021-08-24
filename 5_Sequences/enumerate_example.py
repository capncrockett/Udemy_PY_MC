for index, character in enumerate("abcdefgh"):
    print(index, character)

print("*" * 20)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

print("*" * 20)

index, character = (0, 'a')
print(index)
print(character)
