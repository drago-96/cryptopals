from cryptopals.xor_decrypt import myxor
from cryptopals.encoding import *

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
b1 = bytearray.fromhex(s1)
b2 = bytearray.fromhex(s2)
res = myxor(b1, b2)
print(b2h(res))
