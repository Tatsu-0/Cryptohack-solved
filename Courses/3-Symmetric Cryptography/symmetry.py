import requests

def get_encrypt_flag():
    r = requests.get("https://aes.cryptohack.org/symmetry/encrypt_flag/")
    return r.json()['ciphertext']

def encrypt(plaintext, iv):
    r = requests.get("https://aes.cryptohack.org/symmetry/encrypt/" + plaintext + "/" + iv + "/")
    return r.json()['ciphertext']

plaintext = bytes.fromhex(get_encrypt_flag())
iv = plaintext[:16].hex()
plaintext = plaintext[16:].hex()

print(bytes.fromhex(encrypt(plaintext, iv)).decode())