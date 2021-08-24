menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     for index in range(len(meal) - 1,  -1, -1):
#         if meal[index] == "spam":
#             # print(index)     # for debugging
#             del meal[index]
#     print(meal)
#
# item = "spam"
# for meal in menu:
#     while item in meal:
#         meal.remove(item)
#     print(meal)
#
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()
