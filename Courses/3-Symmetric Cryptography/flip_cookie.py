import requests
import json
from Crypto.Util.Padding import pad

def get_cookie():
    r = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie/")
    return (json.loads(r.text))['cookie']

def check_admin(cookie, iv):
    url = "https://aes.cryptohack.org/flipping_cookie/check_admin/" + cookie + "/" + iv + "/"
    r = requests.get(url)
    return json.loads(r.text)

cookie = get_cookie()
admin_False = "admin=False;"
admin_True = "admin=True;"
padded_False = pad(admin_False.encode(), 16)
padded_True = pad(admin_True.encode(), 16)
iv = ""
cookie_byte = bytes.fromhex(cookie[:32])
for i in range(16):
    number = hex(padded_True[i] ^ padded_False[i] ^ cookie_byte[i])
    if len(number) % 2 == 1:
        iv += "0"
    iv += number[2:]
byte = bytes.fromhex(iv)
flag = check_admin(cookie[32:], iv)
print (flag)