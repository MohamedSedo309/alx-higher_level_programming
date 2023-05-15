#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    c = sentence[0]
    l = len(sentence)
    return (l, c)
