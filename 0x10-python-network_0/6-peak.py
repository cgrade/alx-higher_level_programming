#!/usr/bin/python3
"""Searches for the peak value in an unsroted list of integers"""

def find_peak(list_of_integers):
    """
    Args: List of Integers(int): unsorted lists
    Returns: The peak of the unsorted lists
    """
    size_list = len(list_of_integers)
    mid_val = size_list
    m = size_list //2

    if size_list == 0:
        return None

    else:
        while True:
            mid_val = mid_val //2
            if (m < size_list - 1 and list_of_integers[m] < list_of_integers[m + 1]):
                if mid_val // 2 == 0:
                    mid_val = 2
                m = mid_val // 2
            elif mid_val > 0 and list_of_integers[m] < list_of_integers[m - 1]:
                if mid_val // 2 == 0:
                    mid_val = 2
                m = m -mid_val // 2
            else:
                return list_of_integers[m]
