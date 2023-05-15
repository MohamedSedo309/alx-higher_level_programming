#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    c = sentence[0]
    return (len(sentence), c)
