#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    sum = 0
    for i in range(len(sys.agrv) - 1):
        sum += int(sys.argv[i +1])
    print("{}".format(sum))
