from binascii import unhexlify
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

bytes1 = unhexlify('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
bytes2 = unhexlify('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
bytes3 = unhexlify('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
bytesf = unhexlify('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

key1 = bytes_to_long(bytes1)
key2 = bytes_to_long(bytes2)
key3 = bytes_to_long(bytes3)
flag = bytes_to_long(bytesf)

key2 = key2 ^ key1
key3 = key2 ^ key3
flag = flag ^ key1 ^ key3 ^ key2
ans = long_to_bytes(flag)
print(ans)