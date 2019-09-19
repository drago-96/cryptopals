from cryptopals.encoding import *
from cryptopals.block_cipher import *
from cryptopals.utils import *

class Victim:
    def __init__(self):
        self.key = random_AES_key()

    @staticmethod
    def profile_for(email):
        email = email.replace("&","").replace("=","")
        return "email={}&uid=10&role=user".format(email)

    def get_enc_profile(self, email):
        profile = self.profile_for(email)
        return AES_ECB(profile.encode(), self.key)

    def decrypt_and_parse(self, cipher):
        dec = AES_ECB(cipher, self.key, mode='d')
        return parse_GET(dec.decode())


email = "a@b.com"
victim = Victim()
secret = victim.get_enc_profile(email)

assert victim.decrypt_and_parse(secret)['role'] == 'user'

N = len(victim.profile_for(""))
email1 = "a"*((4-N)%16)
cipher1 = bytearray(victim.get_enc_profile(email1))
print(cipher1)

adm = PKCS7_pad(b"admin")
email2 = "a"*(16-6) + adm.decode()
cipher2 = victim.get_enc_profile(email2)
print(cipher2)

cipher1[-16:] = cipher2[16:32]
print(victim.decrypt_and_parse(cipher1))
