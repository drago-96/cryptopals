from cryptopals.encoding import *
from cryptopals.block_cipher import *
from cryptopals.utils import *

ADMIN = b";role=admin;"
PREPEND = b"comment1=cooking%20MCs;userdata="
APPEND = b";comment2=%20like%20a%20pound%20of%20bacon"

class Victim:
    def __init__(self):
        self.key = random_AES_key()
        self.IV = random_AES_key()

    def encrypt(self, text):
        if b'=' in text or b';' in text:
            raise ValueError("Can't fool me this way!1")
        padded = PREPEND + text + APPEND
        return custom_AES_CBC(padded, self.key, self.IV)

    def is_admin(self, cipher):
        dec = custom_AES_CBC(cipher, self.key, self.IV, mode='d')
        return ADMIN in dec

v = Victim()

assert len(PREPEND) % 16 == 0

enc1 = bytearray(v.encrypt(b'A'*16))
to_xor = myxor(b'A'*16, ADMIN)
enc1[len(PREPEND)-16:len(PREPEND)] = myxor(to_xor, enc1[len(PREPEND)-16:len(PREPEND)])

print(v.is_admin(enc1))
