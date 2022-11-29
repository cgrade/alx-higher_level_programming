#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastD = str(number)[-1]
if number < 0:
    lastD = -int(lastD)
if int(lastD) > 5:
    print(f"Last digit of {number:d} is {lastD:d} and is greater than 5")
elif int(lastD) == 0:
    print(f"Last digit of {number:d} is {lastD:d} and is {lastD:d}")
elif int(lastD) < 6:
    if int(lastD) != 0:
        lastD = int(lastD)
        print(f"Last digit of {number:d} is {lastD:d} and is less than 6 and not 0")
