#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = list()
    new_dict = dict()

    for key in a_dictionary.keys():
        key_list.append(key)
    sortd_keylist = sorted(key_list)
    for item in sortd_keylist:
        new_dict[item] = a_dictionary[item]
    for keys, values in new_dict.items():
        print("{}: {}".format(keys, values))
