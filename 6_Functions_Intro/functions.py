def multiply(x: float, y: float) -> float:
    """Return the product of two variables."""
    # """
    # Multiply 2 numbers.
    #
    # Although this function is intended to multiply 2 numbers,
    # you can also use it to multiply a sequence.  If you pass
    # a string, for example, as the first argument, you'll get
    # the string repeated `y` times as the returned value.
    #
    # :param x: The first number to multiply.
    # :param y: The number to multiply `x` by.
    # :return: The product of `x` and `y`.
    # """
    result = x * y
    return result


def is_palindrome(string):
    # """
    # Determines if a string is a palindrome.
    #
    # The function reverses a string and checks for equality regardless
    # of upper or lowercase.
    #
    # :param string: Must contain alphabetic letters.
    # :return: Bool to check for equality.
    # """
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    # """
    # Casefold and reverse a string and check for equality.
    #
    # The function will add alphabetic characters only to a list, then
    # check for palindrome status.
    #
    # :param sentence: A string of characters.
    # :return: a boolean value to check if string is a palindrome.
    # """
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


answer = multiply(18, 3)
print(answer)


# word = input("Please enter a sentence to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
#
#
# My solution
# def palindrome_sentence(string):
#     letters = ""
#     for char in string:
#         if char.isalpha():
#             letters = letters + char
#     return letters[::-1].casefold() == letters.casefold()
#
#
# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(sentence))


# word = input("Please enter a word to check: ")
# # if is_palindrome(word.casefold()):    I put it here at first. Better in actual function.
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
