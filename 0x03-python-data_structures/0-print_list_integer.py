#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = len(my_list)
    for j in range(0, i):
        print("{:d}".format(my_list[j]))
