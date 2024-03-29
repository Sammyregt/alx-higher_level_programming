#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list
    else:
        # Create a new list by copying the original
        # and replacing the element at the specified index
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
