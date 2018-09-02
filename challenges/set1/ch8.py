from cryptopals.encoding import *
from cryptopals.block_cipher import *

filename = '8.txt'
bs = hexfile_lines_to_bytes(filename)
for b in bs:
    cnt = repeated_AES_chunks(b)
    if cnt > 0:
        print(b2h(b))
