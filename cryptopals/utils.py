import os

lib_dir = os.path.dirname(__file__)


def load_file(filename):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


def myxor(a, b):
    res = []
    for (c, d) in zip(a, b):
        res.append(c ^ d)
    return res


def seq_xor(arr, key):
    i = 0
    res = []
    L = len(key)
    for a in arr:
        res.append(a ^ key[i])
        i = (i + 1) % L
    return res
