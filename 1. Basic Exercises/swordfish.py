while True:
    print('Who are you?')
    name = input()
    
    if name != 'Andrew':
        continue

    print('Hello, Andrew. What is the password?')
    password = input()

    if password == 'swordfish':
        break

print('ACCESS GRANTED')