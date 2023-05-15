#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return nlist
