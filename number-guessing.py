# This is a number guessing game.
import random
secretNumber = random.randint(1, 999)

print('I\'m thinking of a number between 1 and 999, you have 10 guesses!')

# Ask for guesses.
for guessesTaken in range(1, 11):
    print('Take a guess' + '(' + str(guessesTaken) + '):')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break # You guessed correctly!

if guess == secretNumber:
    print('Good job! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry, you ran out of guesses. The number was ' + str(secretNumber) + '!')