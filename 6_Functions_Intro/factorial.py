def factorial(n: int) -> int:
    """Get product of all integers in a series
    from `n` down to 1. Returns an int.

    The factorial function multiplies all whole numbers from the
    chosen number down to 1.

    :param n: Int
    :return: Int
    """
    while n >= 0:
        if n == 0:
            return 1
        for f in range(n - 1, 0, -1):
            n = f * n
        else:
            return n


for i in range(36):
    print(i, factorial(i))

# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
#
#     return result

# Recursive Solution:
# def factorial(n: int) -> int:
#     """
#     Return n! (0! is 1).
#
#     Valid for `n` in the range 0 to 998 (inclusive).
#     Larger values of `n` will cause a RecursionError.
#     """
#     if n <= 1:
#         return 1
#
#     return n * factorial(n - 1)
