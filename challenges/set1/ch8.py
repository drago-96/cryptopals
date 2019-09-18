from cryptopals.encoding import *
from cryptopals.block_cipher import *

filename = '8.txt'
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, filename)

bs = hexfile_lines_to_bytes(abs_file_path)
for b in bs:
    cnt = repeated_AES_chunks(b)
    if cnt > 0:
        print(b2h(b))
