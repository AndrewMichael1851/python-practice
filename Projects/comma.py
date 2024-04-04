'''
Comma Values
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with "and" inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''

# Create the list.
myList = []

# Build the list.
while True:
    print('Please type a new list item.')
    newListItem = input()

    if newListItem == '':
        print('Error: Please restart the program and use a valid entry.')
        break

    if newListItem not in myList:
        myList.append(newListItem)

        if len(myList) > 2:
            for item in myList[:-1]:
                print(item + ', ', end='')
            print('and ' + myList[-1])
        
        elif len(myList) == 2:
            print(myList[0] + ' and ' + myList[1])
        
        elif len(myList) == 1:
            print(myList[0])

        else:
            print('Please add a valid input.')