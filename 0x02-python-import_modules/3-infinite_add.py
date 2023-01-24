#!/usr/bin/python3
from sys import argv

for i in range(1, len(argv)):
    count = 0
    while count <= len(argv):
        summ = int(argv[i]) + count
        count += 1
    print(summ)
