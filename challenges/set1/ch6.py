from cryptopals.xor_decrypt import *
from cryptopals.encoding import *


script_dir = os.path.dirname(__file__)
filename = '6.txt'
abs_file_path = os.path.join(script_dir, filename)

with open(abs_file_path, 'r') as f:
    lines = f.readlines()
content = ''.join([line.strip() for line in lines])

b = base64.b64decode(content)
ba = bytearray(b)
L = len(ba)

#freqs = load_frequencies()

keys = find_keysize(ba)
print("Possible keysizes: ", keys)

KS = keys[0]

tutti = [[ba[KS*j+i] for j in range(L//KS)] for i in range(KS)]

key = []

for block in tutti:
    L = len(block)
    max = 0
    for i in range(255):
        res = seq_xor(block, [i])
        en = english(res)
        if en > max:
            max = en
            idx = i
    key.append(idx)


fin_res = seq_xor(ba, key)
print("Key found: \"{}\"".format(b2utf8(key)))
print()
print("Decoded text:")
print(b2utf8(fin_res))
