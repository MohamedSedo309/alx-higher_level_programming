#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            div = float(val1) / float(val2)
        except (ZeroDivisionError):
            print("division by 0")
            div = 0
        except (TypeError):
            print("wrong type")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
