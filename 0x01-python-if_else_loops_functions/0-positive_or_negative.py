#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#if the number is greater than 0: is positive
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
