d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v)    # => list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for k, v, in d.items():
    if v == "four":
        print(f"{d[k]} was found with the key {k}")

# Code for "The dict `update` method" lecture.
# ********************************************
#
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three",
# }
# d.update(d2)
# for k, v in d.items():
#     print(k, v)
#
# print()
#
# d.update(enumerate(pantry_items))
# for k, v, in d.items():
#     print(k, v)

# Code for "The remaining `dict` methods" lecture.
# ************************************************
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

# keys = d.keys()
# print(keys)

# for item in d.keys():
#     print(item)

