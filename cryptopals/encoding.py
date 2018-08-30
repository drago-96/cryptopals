import base64


def b2u8(b):
    return bytes(b).decode('utf-8')


def b2h(b):
    return bytes(b).hex()
