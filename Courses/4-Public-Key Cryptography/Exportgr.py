from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

p = 16007670376277647657 
g = 2
A = 3480984767542299599
B = 4799319123249983925
a = 3512837750098271107 #https://www.alpertron.com.ar/DILOG.HTM

shared_secret = pow(B, a, p)
iv = 'b44a83e7fccf7067a4fb2e0c4aec9bdd'
ciphertext = '9b5b125a94f968ba66793b605bda8efa5fcedb4886e01b4fefba70625b0d6c07'

print(decrypt_flag(shared_secret, iv, ciphertext))
