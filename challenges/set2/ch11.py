from cryptopals.encoding import *
from cryptopals.block_cipher import *


howmany = 20
zeros = b'\0' * 16 * howmany
right = 0
N = 100
for _ in range(N):
    enc, mode = encryption_oracle(zeros)
    cnt = repeated_AES_chunks(enc)
    if cnt > 0.5 * howmany:
        det_mode = "ECB"
    else:
        det_mode = "CBC"
    if det_mode == mode:
        right += 1
print(right / N)
