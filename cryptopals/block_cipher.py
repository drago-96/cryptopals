from Crypto.Cipher import AES


def AES_ECB(text, key, mode='e'):
    cipher = AES.new(key, AES.MODE_ECB)
    if mode == 'e':
        return cipher.encrypt(text)
    if mode == 'd':
        return cipher.decrypt(text)
