from cryptopals.xor_decrypt import *
from cryptopals.encoding import *

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
b = bytearray.fromhex(s)

max = 0
for i in range(255):
    res = seq_xor(b, [i])
    e = english(res)
    if e > max:
        max = e
        idx = i

print(b2u8(seq_xor(b, [idx])))
