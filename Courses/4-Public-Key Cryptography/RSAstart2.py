import math

b = 12
e = 65537
p, q = 17,23
N = p * q
print(pow(b, e, N))