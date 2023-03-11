#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        sentence[0] = None
    tuple_formed = (len(sentence), sentence[0])
    return tuple(tuple_formed)


if __name__ == '__main__':
    multiple_returns(sentence)
