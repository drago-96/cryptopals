from Crypto.Cipher import AES
from cryptopals.utils import myxor
import os
import random
import base64


def PKCS7_pad(text, bl):
    ba = bytearray(text)
    r = len(ba) % bl
    if r == 0:
        return ba
    else:
        toadd = bl - r
        if toadd > 255:
            raise Exception("Too many bytes to pad")
        return ba + bytearray([toadd] * toadd)


def AES_ECB(text, key, mode='e'):
    cipher = AES.new(key, AES.MODE_ECB)
    text = bytes(PKCS7_pad(text, 16))
    if mode == 'e':
        return cipher.encrypt(text)
    if mode == 'd':
        return cipher.decrypt(text)


def custom_AES_CBC(text, key, IV, mode='e'):
    padded = PKCS7_pad(text, 16)
    prev = IV
    res = bytearray([])
    for i in range(0, len(padded), 16):
        chunk = padded[i:i+16]
        if mode == 'e':
            x = myxor(chunk, prev)
            prev = bytearray(AES_ECB(bytes(x), key, mode='e'))
            res.extend(prev)
        if mode == 'd':
            dec = bytearray(AES_ECB(bytes(chunk), key, mode='d'))
            res.extend(myxor(prev, dec))
            prev = chunk
    return res


def random_AES_key():
    return os.urandom(16)


def encryption_oracle(text):
    ba = bytearray(text)
    res = bytearray(os.urandom(random.randint(5, 10)))
    res += ba
    res += bytearray(os.urandom(random.randint(5, 10)))
    key = random_AES_key()
    if random.randint(0, 1) == 0:
        enc = AES_ECB(bytes(res), key)
        mode = "ECB"
    else:
        enc = custom_AES_CBC(bytes(res), key, random_AES_key())
        mode = "CBC"
    return enc, mode


def repeated_AES_chunks(text, bl=16):
    cnt = 0
    ba = bytes(text)
    s = set()
    for i in range(0, len(ba), bl):
        chunk = ba[i:i+bl]
        if chunk in s:
            cnt += 1
        else:
            s.add(chunk)
    return cnt


def padded_ECB(text, key):
    s = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg \
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq \
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg \
        YnkK"
    b = base64.b64decode(s)
    ba = bytearray(text)
    ba += bytearray(b)
    return AES_ECB(ba, key)
