from cryptopals.encoding import *
from cryptopals.block_cipher import *

script_dir = os.path.dirname(__file__)
filename = '7.txt'
abs_file_path = os.path.join(script_dir, filename)

b = b64file_to_bytes(abs_file_path)
key = b'YELLOW SUBMARINE'
res = AES_ECB(b, key, mode='d')
print(b2utf8(res))
