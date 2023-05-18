#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    nlist = my_list[:]
    for i in range(len(nlist)):
        nlist[i] *= number
    return nlist
