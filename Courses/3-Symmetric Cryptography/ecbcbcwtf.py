import requests

def encrypt_flag():
    r = requests.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/")
    return r.json()["ciphertext"]

def decrypt_flag(ciphertext):
    r = requests.get("https://aes.cryptohack.org/ecbcbcwtf/decrypt/" + ciphertext)
    return r.json()["plaintext"]

encrypted = encrypt_flag()
decrypted = decrypt_flag(encrypted)
b1 = bytes.fromhex(encrypted[:len(encrypted) - 32])
b2 = bytes.fromhex(decrypted[32:])
flag = ""
for i in range(len(b1)):
    flag += chr(b1[i] ^ b2[i])
print (flag)