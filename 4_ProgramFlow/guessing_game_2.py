answer = 5

print("Please guess a number between 1 and 10: ")
guess1 = int(input())

if guess1 < answer:
    print("Please guess higher")
    guess2 = int(input())
    if guess2 == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly. "
              "You guessed {0} and {1}.".format(guess1, guess2))
elif guess1 > answer:
    print("Please guess lower")
    guess2 = int(input())
    if guess2 == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly. "
              "You guessed {0} and {1}.".format(guess1, guess2))
else:
    print("You got it first time")
