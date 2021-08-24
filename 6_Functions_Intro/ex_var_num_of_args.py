def sum_numbers(*args: float) -> float:
    """
    get the sum of a tuple

    :param args: a tuple of floats
    :return: the sum of arguments
    """
    # for x in args:
    #     return sum(args)
    #
    # OR
    #
    result = 0
    for number in args:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
