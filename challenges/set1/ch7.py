from cryptopals.encoding import *
from cryptopals.block_cipher import *

filename = '7.txt'
b = b64file_to_bytes(filename)
key = b'YELLOW SUBMARINE'
res = AES_ECB(b, key, mode='d')
print(res)
