#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if type(number) is int:
    last_digit = str(number)[len(str(number)) - 1]
    last = int(last_digit)
    if number < 0:
        last *= -1
    if last > 5:
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif last < 6 and last != 0:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
    elif last == 0:
        print(f"Last digit of {number} is {last} and is 0")
else:
    raise TypeError("Only integers are allowed")
