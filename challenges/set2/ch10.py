from cryptopals.encoding import *
from cryptopals.block_cipher import *

with open('10.txt', 'r') as f:
    content = f.read()
b = base64.b64decode(content)
key = b'YELLOW SUBMARINE'
IV = bytearray([0]*16)
res = custom_AES_CBC(b, key, IV, mode='d')

msg = b'Sopra la panca la capra campaaaa'
enc = custom_AES_CBC(msg, key, IV, mode='e')
assert msg == custom_AES_CBC(enc, key, IV, mode='d')

print(b2utf8(res))
