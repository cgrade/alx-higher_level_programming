#!/usr/bin/python3
if __name__ == "__main__":
    """Prints out the arguments entered into the command line and list them out"""
    import sys
    arg = sys.argv
    num_of_arg = len(arg) - 1
    if num_of_arg == 0:
        print("{} argument.".format(num_of_arg))
    elif num_of_arg == 1:
        print("{} argument:".format(num_of_arg))
    else:
        print("{} arguments:".format(num_of_arg))
    for i, item in enumerate(arg):
        if i > 0:
            print("{}: {}".format(i, item))
