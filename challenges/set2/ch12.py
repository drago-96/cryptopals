from cryptopals.encoding import *
from cryptopals.block_cipher import *


# Get block size
key = random_AES_key()
a = b'A'
s = b''
base_enc = padded_ECB(s, key)
N = len(base_enc)
BS = 0
for i in range(1, 100):
    s += a
    enc = padded_ECB(s, key)
    if len(enc) != N:
        N = len(enc)
        diff = i
    if enc[i:2*i] == base_enc[0:i]:
        BS = i
        print("Block size", i)
        break

N = len(base_enc)-diff
print(N)

# Is ECB?
howmany = 20
zeros = b'\0' * BS * howmany
enc = padded_ECB(zeros, key)
if repeated_AES_chunks(enc) > 0.5 * howmany:
    print("ECB")


res = bytearray(b'A' * (BS-1))

# One byte short
for block_num in range(N//BS+1):
    for j in range(BS):
        if block_num*BS+j > N:
            break
        aas = bytearray(b'A' * (BS-j-1))
        base_enc = padded_ECB(aas, key)
        for i in range(256):
            test = res[(block_num)*BS+j:(block_num+1)*BS+j-1] + bytearray([i])
            enc = padded_ECB(test, key)
            if enc[0:BS] == base_enc[block_num*BS:(block_num+1)*BS]:
                char = i
                break
        res.append(i)

print(b2utf8(res[15:]))
