#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = last_digit * -1
string_build = f"Last digit of {number:d} is {last_digit:d} "
if last_digit > 5:
    string_build = string_build + "and is greater than 5"
elif last_digit == 0:
    string_build = string_build + "and is 0"
elif last_digit < 6 and last_digit > 0:
    string_build = string_build + "and is less then 6 and not 0"
print(string_build)
