#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        resul = []
        for i in range(len(my_list)):
            if my_list[i] % 2:
                resul.append(False)
            else:
                resul.append(True)
        return resul
