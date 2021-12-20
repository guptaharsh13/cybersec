import math

num = int(input("num = "))
print()

coprimes = []
for i in range(2, num):
    if math.gcd(i, num) == 1:
        coprimes.append(i)

print(", ".join([str(num) for num in coprimes]))
