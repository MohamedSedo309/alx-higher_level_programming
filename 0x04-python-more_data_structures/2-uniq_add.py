#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = []
    for i in range(len(my_list)):
        if my_list[i] not in lis:
            lis.append(my_list[i])
    return sum(lis)
