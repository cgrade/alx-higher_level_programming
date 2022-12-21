#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    for n in range(list_length):
        try:
            nlist.append(my_list_1[n] / my_list_2[n])
        except ZeroDivisionError:
            print("division by 0")
            nlist.append(0)
        except TypeError:
            print("wrong type")
            nlist.append(0)
        except IndexError:
            print("out of range")
            nlist.append(0)
        finally:
            pass
    return(nlist)
