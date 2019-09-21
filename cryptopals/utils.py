import os
from itertools import zip_longest

lib_dir = os.path.dirname(__file__)


def load_file(filename):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


# XOR of two bytearrays, not necessarily of same length
def myxor(a, b, fill=True):
    res = []
    if fill:
        couples = zip_longest(a,b,fillvalue=0)
    else:
        couples = zip(a,b)
    for (c, d) in couples:
        res.append(c ^ d)
    return bytearray(res)


# repeating XOR cipher
def seq_xor(arr, key):
    i = 0
    res = []
    L = len(key)
    for a in arr:
        res.append(a ^ key[i])
        i = (i + 1) % L
    return bytearray(res)


# parse GET arguments
def parse_GET(query):
    res = {}
    for s in query.split("&"):
        k, v = s.split("=")
        res[k] = v
    return res
