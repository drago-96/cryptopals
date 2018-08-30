from cryptopals.encoding import *
from cryptopals.block_cipher import *

filename = '8.txt'
bs = hexfile_lines_to_bytes(filename)
for b in bs:
    s = set()
    cnt = 0
    for i in range(0, len(b), 16):
        chunk = b[i:i+16]
        if chunk in s:
            cnt += 1
        else:
            s.add(chunk)
    if cnt > 0:
        print(b2h(b))
