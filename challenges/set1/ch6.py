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

freqs = load_frequencies()

keys = find_keysize(ba)
print("Possible keysizes: ", keys)

KS = keys[0]

tutti = [[ba[KS*j+i] for j in range(L//KS)] for i in range(KS)]

ch = []

for block in tutti:
    L = len(block)
    min = 10000
    for i in range(255):
        # chi = [i]*l
        res = seq_xor(block, [i])
        en = en_dist(res, freqs)
        if en < min:
            min = en
            idx = i
    #     print(res)
    #     e, e2 = english(res)
    #     most = sorted(range(len(e)),key=e.__getitem__,reverse=True)
    #     print(most[0:10])
    #     englishness.append((i,e2))
    #     if len(set(most[0:11]).intersection(englishmost))>3:
    #         print(i)
    #         possibili.append(i)
    # print(possibili)
    # print(englishness)
    # sidx = [i[0] for i in sorted(englishness, key=lambda x:-x[1])]
    # print(sidx[0:10])
    # chiavi.append( list(set(possibili).intersection(set(sidx[0:10]))) )
    # chiavi.append(sidx[0:3])
    # print(bytes(seq_xor(block, [sidx[0]])))
    ch.append(idx)

'''
Key:
[116, 111, 114, 32, 88, 58, 32, 66, 114, 105, 110, 103, 32, 116, 104, 101, 32,
    110, 111, 105, 115, 101, 84, 101, 114, 109, 105, 110, 97]
'''

fin_res = seq_xor(ba, ch)
print("Key found: \"{}\"".format(b2u8(ch)))
print()
print("Decoded text:")
print(b2u8(fin_res))
