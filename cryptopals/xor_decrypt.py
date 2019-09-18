import math
import json
import random

from cryptopals.utils import *

# CONSTANTS

alphabet = list(range(65, 91))+list(range(97, 123))  # upper + lower
others = [32, 33, 34, 39]
numbers = list(range(48, 58))
eng_alph = others + numbers + alphabet


# FUNCTIONS


def load_frequencies():
    with open(load_file('files/letter_freq.json'), 'r') as f:
        frequencies = json.load(f)
    allfreq = [0]*256
    for k, v in frequencies.items():
        allfreq[ord(k)] = v/10
    return allfreq


def count_good_chars(seq, chars):
    cnt = 0.
    for i in seq:
        if i in chars:
            cnt += 1
    return cnt/len(seq)


def english(seq):
    return count_good_chars(seq, eng_alph)


def numbits(x):
    cnt = 0
    for _ in range(8):
        cnt += x & 1
        x >>= 1
    return cnt


def hamming_distance(a, b):
    xor = myxor(a, b)
    cnt = 0.
    for i in xor:
        cnt += numbits(i)
    return cnt


def dist(x, y):
    s = 0.
    for (xi, yi) in zip(x, y):
        s += (xi - yi)**2
    return math.sqrt(s)


def en_dist(seq, freq):
    fs = [0]*256
    for i in seq:
        fs[i] += 1
    t = sum(fs)
    for i in range(256):
        fs[i] = fs[i] * 1. / t
    return dist(freq, fs)


def find_keysize(cipher, first=2, last=40):
    values = []
    L = len(cipher)
    for keysize in range(first, last+1):
        chunks = []
        for i in range(0, L, keysize):
            chunks.append(cipher[i:keysize + i])
        distances = []
        # from itertools import combinations
        # for p in combinations(range(len(chunks)), r=2):
        #     d = hamming_distance(chunks[p[0]], chunks[p[1]])
        for _ in range(len(chunks)*3):
            a, b = random.randint(0, len(chunks)-1), random.randint(0, len(chunks)-1)
            d = hamming_distance(chunks[a], chunks[b])
            distances.append(d / keysize)
        values.append(sum(distances) / len(distances))
    most = sorted(range(len(values)), key=values.__getitem__)
    return [m+first for m in most]
