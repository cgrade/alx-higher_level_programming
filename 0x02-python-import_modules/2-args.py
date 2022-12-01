#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    list_c = len(sys.argv) - 1
    if list_c == 0:
        print("0 arguments.")
    elif list_c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(list_c))
    for i in range(list_c):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
