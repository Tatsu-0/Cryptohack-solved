import math

p = [i for i in range(1,29) if math.gcd(29,i) == 1]
int = [14, 6, 11]
for i in (p):
    for j in int:
        for k in range(1,100):
            if (pow(i,2) - j == k*29):
                print(i)