from cryptopals.xor_decrypt import *
from cryptopals.encoding import *

s = "Burning 'em, if you ain't quick and nimble \
I go crazy when I hear a cymbal"
b = bytearray(s, 'ascii')
kb = bytearray("ICE", 'ascii')

r = seq_xor(b, kb)
print(b2h(r))
