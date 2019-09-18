from cryptopals.encoding import *
from cryptopals.block_cipher import *

b = b'YELLOW SUBMARINE'
block_length = 20
padded = PKCS7_pad(b, block_length)

print(bytes(padded))
