#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def principal():
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if (argv[2]) not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

