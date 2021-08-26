from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original
    values.
    """

    # CODE HERE
    deep_d = {}
    keys = []
    values = []
    for k, v in d.items():
        deep_d[k] = v
        # keys.append(k)
        # print(type(k))
        # values.append(v)
        # print(type(v))
    # print(type(keys))
    # print(keys)
    # print(type(values))
    # print(values)
    # print(type(deep_d))
    # print(deep_d)
    # for k, v in deep_d.items():
    #     print(type(k))
    #     print(type(v))
    return deep_d


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
