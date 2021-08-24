def fizz_buzz(n: int) -> str:
    """
    Check if `n` is divisible by 3, 5, or both.

    This function is a fun way to check for divisibility of a number.
    It returns fizz, buzz, or fizz buzz depending on the result.

    :param n: Int
    :return: `string` "fizz" if divisible by 3, "buzz" if divisible
        by 5, or "fizz buzz" if divisible by 3 and 5.
    """

    if n % 3 and n % 5 != 0:
        n = str(n)
    elif n % 3 == 0 and n % 5 == 0:
        n = "fizz buzz"
    elif n % 3 == 0:
        n = "fizz"
    elif n % 5 == 0:
        n = "buzz"
    return n


for i in range(1, 101):
    print(fizz_buzz(i))
