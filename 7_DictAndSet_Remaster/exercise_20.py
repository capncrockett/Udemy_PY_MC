# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
# for char in text.casefold():
for char in text.lower():
    if char.isalpha():
        word_count[char] = word_count.setdefault(char, 0) + 1
        # shop_list[item] = shop_list.setdefault(item, 0) + quantity

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
