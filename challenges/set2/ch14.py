from cryptopals.encoding import *
from cryptopals.block_cipher import *
from cryptopals.utils import *

import random

class Oracle:
    def __init__(self):
        self.key = random_AES_key()
        self.prefix = os.urandom(random.randint(1,100))

    def encrypt(self, text):
        return padded_ECB(self.prefix+text, self.key)

o = Oracle()

aas = b'A' * 16 * 3
res = o.encrypt(aas)
for i in range(0, len(res), 16):
    if res[i:i+16] == res[i+16:i+32]:
        pad_bl = i
        aas_enc = res[i:i+16]

for i in range(16,32):
    aas = b'A' * i
    res = o.encrypt(aas)
    if res[pad_bl:pad_bl+16] == aas_enc:
        padding_length = pad_bl - i + 16
        missing = i-16
        break

res = bytearray(b'A' * 15)
maas = bytearray(b'A' * missing)

N = len(o.encrypt(b''))
for i in range(16):
    c = o.encrypt(b'A'*i)
    if len(c) != N:
        N = len(c) - i - padding_length - 16
        break

# One byte short
for block_num in range(N//16+1):
    for j in range(16):
        if block_num*16+j > N+1:
            break
        aas = bytearray(b'A' * (16-j-1))
        base_enc = o.encrypt(maas+aas)
        for i in range(256):
            test = maas + res[(block_num)*16+j:(block_num+1)*16+j-1] + bytearray([i])
            enc = o.encrypt(test)
            if enc[pad_bl:pad_bl+16] == base_enc[pad_bl+block_num*16:pad_bl+(block_num+1)*16]:
                char = i
                break
        res.append(i)

print(b2utf8(PKCS7_strip(res)))
