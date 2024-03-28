import random

def func(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

for i in range(1, 11):
    num = random.randint(-3, 3)
    print(func(num))