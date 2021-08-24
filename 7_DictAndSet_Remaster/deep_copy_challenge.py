from contents import recipes


# Write a function that takes a dictionary as an argument, return a deep
#   copy of the dictionary.
def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """
    # Create an empty dictionary.
    copy_dict = {}

    # Iterate over keys and values of dict being copied.
    
    copy_dict.update()
        # For each key, copy the value, add value to new dict.
        # copy_dict = d.copy()  # Won't work. Makes shallow copy.
    return my_deepcopy(copy_dict)

# Function only has to handle values that are dicts or lists. Both have
#   a `copy` method ;)

# TO TEST FUNCTION
recipes_copy = my_deepcopy(recipes)
print(recipes_copy)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
print(id(recipes_copy))
print(id(recipes))
