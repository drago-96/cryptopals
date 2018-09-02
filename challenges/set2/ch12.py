from cryptopals.encoding import *
from cryptopals.block_cipher import *


# Get block size
key = random_AES_key()
a = b'A'
s = b''
base_enc = padded_ECB(s, key)
for i in range(1, 100):
    s += a
    enc = padded_ECB(s, key)
    if enc[i:2*i] == base_enc[0:i]:
        print("Block size", i)
        break

# Is ECB?
howmany = 20
zeros = b'\0' * 16 * howmany
enc = padded_ECB(zeros, key)
if repeated_AES_chunks(enc) > 0.5 * howmany:
    print("ECB")

# One byte short
aa = b'A' * 15
base_enc = padded_ECB(aa, key)
for i in range(256):
    test = aa + bytearray([i])
    enc = padded_ECB(test, key)
    if enc[0:16] == base_enc[0:16]:
        char = i
        break

print(char)
