#!/usr/bin/python3
def no_c(my_string):
    listnew = []
    for i in my_string:
        if i != 'c' and i != 'C':
            listnew.append(i)
    return ''.join(listnew)
