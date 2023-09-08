#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence_len == 0:
        res = (sentence_len, None)
    else:
        res = (sentence_len, sentence[0])

    return res
