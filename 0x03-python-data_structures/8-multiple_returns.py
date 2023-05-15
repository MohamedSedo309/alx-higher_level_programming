#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    c = sentence[0]
    if c == None:
        return (0, None)
    else:
        return (l, c)
