#!/usr/bin/python3
"""

This module is composed of a function that add two integers together

"""
def add_integer(a, b =98):
    """Function that add two integers or float together

    Args:
    a: first number
    b: second number

    Returns:
        The sum of the two given numbers

    Raises:
        TypeError: If a or b aren't an integer or a float

    """
    
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an  integer")
    a = int(a)
    b = int(b)
    return (a + b)
