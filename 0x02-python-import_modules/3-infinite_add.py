#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    output = 0
    for i in range(len(sys.argv) - 1):
        output += int(sys.argv[i + 1])
    print("{}".format(output))
