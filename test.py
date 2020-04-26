from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

privatekey = RSA.generate(2048)
privatekey_final = bytes(privatekey.exportKey('PEM'))
publickey = privatekey.publickey()
publickey_final = bytes(publickey.exportKey('PEM'))


