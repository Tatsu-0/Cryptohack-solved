import math

def generator(g, p):
    for n in range(2, p):
        if pow(g, n, p) == g:
            return False
    return True
    
p = 28151
for g in range(p):
    if generator(g, p):
        print(g)
        break
