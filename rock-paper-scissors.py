# A basic rock-paper-scissors game!
import random, sys

print('ROCK, PAPER, SCISSORS')

# Scorecard.
wins = 0
losses = 0
ties = 0

# Main game loop.
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()

        if playerMove == 'q':
            sys.exit() # to quit the program
        elif playerMove in ('r', 'p', 's'):
            break # to break the player input loop
        print('Type one of r, p, s, or q.')

        # Display what the player chose.
        if playerMove == 'r':
            print('ROCK versus...')
        elif playerMove == 'p':
            print('PAPER versus...')
        elif playerMove == 's':
            print('SCISSORS versus...')
        else:
            print('ERROR')

        # Display the computer's choice.
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'r'
            print('ROCK')
        elif randomNumber == 2:
            computerMove = 'p'
            print('PAPER')
        elif randomNumber == 3:
            computerMove = 's'
            print('SCISSORS')

        ### NEED TO PICK UP HERE
        