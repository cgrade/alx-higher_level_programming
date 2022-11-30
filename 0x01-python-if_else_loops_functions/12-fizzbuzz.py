#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 and num % 5 == 0:
            print("fizzbuzz", end=" ")
        elif num % 3 == 0:
            print("fizz", end=" ")
        elif num % 5 == 0:
            print("buzz", end=" ")
        else:
            print(num, end=" ")
    
