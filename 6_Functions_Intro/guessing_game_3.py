import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else: this isn't even needed!
        print("{0} is not a number...".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0  # Initialise to any number that doesn't equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        if guess == 0:
            break

        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # if guess == 0:
        #     print("you have quit")
        #     break
#
#
# import random
#
# highest = 10
# answer = random.randint(1, highest)
# print(answer)   # TODO: Remove after testing
#
# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())
#
# # if guess == answer:
# #     print("You got it first time")
#
# while guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     if guess == 0:
#         print("you have quit")
#         break
#