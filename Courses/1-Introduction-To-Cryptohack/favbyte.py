from binascii import unhexlify
from Crypto.Util.number import bytes_to_long


favhex = unhexlify('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for xor_key in range(30):
    decoded = ''.join(chr(b ^ xor_key) for b in favhex)
    if decoded.isprintable():
        print(xor_key, decoded)