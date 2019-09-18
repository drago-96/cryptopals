from cryptopals.xor_decrypt import *
from cryptopals.encoding import *
import os

script_dir = os.path.dirname(__file__)
filename = '4.txt'
abs_file_path = os.path.join(script_dir, filename)

with open(abs_file_path, 'r') as f:
    max = 0
    for line in f:
        s = line.strip()
        b = bytearray.fromhex(s)
        for i in range(255):
            res = seq_xor(b, [i])
            e = english(res)
            if e > max:
                max = e
                idx = i
                bx = b

print(b2utf8(seq_xor(bx, [idx])), max)
