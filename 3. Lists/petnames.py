# Base list.
myPets = []

# Iterate.
while True:
    # Prompt for a pet name.
    print('Enter a pet name to add it to the list.')
    name = input()

    if name not in myPets:
        myPets.append(name)
        print(name + ' has been added to the register!')
        myPets.sort() # Sort in ASCIIbetical order.
        print('Your pets are:')
        for name in myPets:
            print(' ' + name)
    elif name in myPets:
        print(name + ' already exists in the register!')
        print('Your pets are:')
        for name in myPets:
            print(' ' + name)
    else:
        print('ERROR')
