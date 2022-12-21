#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        if type(my_list[i]) != str():
            try:
                print("{:d}".format(my_list[i]), end='')
            except Exception:
                pass
        else:
            continue
        n += 1
    print()
    return n
