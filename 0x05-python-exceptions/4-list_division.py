#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    i = 0
    for n in my_list_1:
        try:
            a = n / my_list_2[i]
            nlist.append(a)
        except ZeroDivisionError:
            print("division by 0")
            nlist.append(0)
        except TypeError:
            print("wrong type")
            nlist.append(0)
        except IndexError:
            print("out of range")
            nlist.append(0)
        i += 1
    return(nlist)
