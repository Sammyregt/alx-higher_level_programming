#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char.lower() != 'c':
            new_string += char

    return new_string)
