'''
The Collatz Sequence
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
'''

# Collatz sequence.
def collatz(number):
    if number % 2 == 0:
        number = number / 2
    elif number % 2 == 1:
        number = (3 * number) + 1
    return number

# User input.
while True:
    print('Please select a starting number.')
    try:
        userInput = float(int(input()))

        print('You chose: ' + str(userInput))

        # Loop.
        while userInput != 1:
            print(userInput)
            userInput = collatz(userInput)

        # Print the final number.
        print('You reached ' + str(userInput))
        break

    except:
        print('Please choose an integer.')
