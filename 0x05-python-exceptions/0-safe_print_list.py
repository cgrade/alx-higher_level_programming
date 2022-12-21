#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(1, x+1):
            print(i, end='')
        print()
    except Exception:
        pass
    return(x)
