#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, subtraction, mulitplication and division of 10 and 5."""
    import calculator_1
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
