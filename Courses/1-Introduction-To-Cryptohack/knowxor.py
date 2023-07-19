from binascii import unhexlify

def brute(input, key):
    if len(input) != len(key):
        return "Failed!"

    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(data)
print("\n1. CIPHER IN HEX: {}".format(cipher))

key_part = brute(cipher[:7], "crypto{".encode())
print("\n2. PARTIAL KEY: {}".format(key_part))

key = (key_part + "y").encode()
key += key * int((len(cipher) - len(key))/len(key))
key += key[:((len(cipher) - len(key))%len(key))]
print("\n3. DECODING USING FULL KEY: {}".format(key))

plain = brute(cipher, key)
print("\n4. FLAG: {}\n".format(plain))