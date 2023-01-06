#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp_a = list(tuple_a)
    tp_b = list(tuple_b)
    if len(tp_a) == 1:
        tp_a = (tp_a[0], 0)
    elif len(tp_a) == 0:
        tp_a = (0, 0)
    if len(tp_b) == 1:
        tp_b = (tp_b[0], 0)
    elif len(tp_b) == 0:
        tp_b = (0, 0)
    return (tp_a[0] + tp_b[0], tp_a[1] + tp_b[1])
