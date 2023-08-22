#run in linux terminal
import requests
from pwn import xor

png = bytes.fromhex('89504e470d0a1a0a0000000d49484452')

def get_ciphertext():
    r = requests.get("https://aes.cryptohack.org/bean_counter/encrypt/")
    return r.json()['encrypted']

ct = bytes.fromhex(get_ciphertext())
key = xor(png, ct[:16])
pt = xor(ct, key)

with open('bean_flag.png', 'wb') as fd:
    fd.write(pt)
    