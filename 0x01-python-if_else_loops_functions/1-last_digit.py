#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastD = str(number)[-1]
if number < 0:
    lastD = -int(lastD)
lastD = int(lastD)
if lastD > 5:
    lastD = int(lastD)
    print(f"Last digit of {number:d} is {lastD:d} and is greater than 5")
elif lastD == 0:
    lastD = int(lastD)
    print(f"Last digit of {number:d} is {lastD:d} and is {lastD:d}")
elif lastD < 6:
    lastD = int(lastD)
    if lastD != 0:
        lastD = lastD
        print(f"Last digit of {number:d} is {lastD:d}"
        " and is less than 6 and not 0")
