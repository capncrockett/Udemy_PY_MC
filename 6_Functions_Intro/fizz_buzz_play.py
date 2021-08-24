def fizz_buzz(n: int) -> str:
    """
    Play Fizz buzz

    This function is a fun way to check for divisibility of a number.
    It returns fizz, buzz, or fizz buzz depending on the result.

    :param n: Int
    :return: `string` "fizz" if divisible by 3, "buzz" if divisible
        by 5, or "fizz buzz" if divisible by 3 and 5.
    """

    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


print(input("Let's play Fizz Buzz. Press ENTER to start: "))
print()

counter = 0

while counter < 99:
    # CPU turn
    counter += 1
    correct_answer = fizz_buzz(counter)
    print(correct_answer)

    counter += 1
    correct_answer = fizz_buzz(counter)

    # player turn
    user_answer = input("What comes next?: ")
    # user_answer = correct_answer
    if user_answer == correct_answer:
        print(user_answer, "is correct.")
    else:
        print("Sorry, the correct answer was {}".format(correct_answer))
        break
else:
    print("Congratulations! You made it to {}!!!".format(counter))
