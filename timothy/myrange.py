#!/usr/bin/python3

'''
create the myrange function

parameter:
    start: value start
    stop: stop value
    step: step value

'''

def myrange(*, start=None, stop, step = None):
    # seting the start = 0
    # setting step = 1
    if start is None:
        start = 0

    if step is None:
        step = 1

    # creating an empty list to store the result
    rag = []

    # loop and append the result to the list
    while (start < stop + step):
        rag.append(start)
        start += step

    return (rag)
