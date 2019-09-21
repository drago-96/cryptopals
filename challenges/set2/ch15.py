from cryptopals.block_cipher import *

assert PKCS7_strip(b"ICE ICE BABY\x04\x04\x04\x04") == b"ICE ICE BABY"

try:
    PKCS7_strip(b"ICE ICE BABY\x05\x05\x05\x05")
    PKCS7_strip(b"ICE ICE BABY\x01\x02\x03\x04")
except ValueError:
    print("OK")
