print("\n\nCALCULATE num1 mod num2\n")
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))

a1 = 1
a2 = 0
a3 = num2
b1 = 0
b2 = 1
b3 = num1

print("\n\nA1 = 1")
print("A2 = 0")
print(f"A3 = {num2}")
print("B1 = 0")
print("B2 = 1")
print(f"B3 = {num2}")

if b3 == 0:
    print("\n\nB3 == 0")
    print("\nThus,")
    print(f"GCD({num1}, {num2}) = {a3}")
    print("NO INVERSE")
    exit(0)

print("\nB3 not = 0")

if b3 == 1:
    print("\n\nB3 == 1")
    print("\nThus,")
    print(f"GCD({num1}, {num2}) = B3 = {b3}")
    print(f"MMI of {num1} under {num2} = B2 = {b2}")
    exit(0)

print("\nB3 not = 1")

print("\n\n\tQ\tA1\tA2\tA3\tB1\tB2\tB3\tT1\tT1\tT3\n")
print(f"\t-\t{a1}\t{a2}\t{a3}\t{b1}\t{b2}\t{b3}\t-\t-\t-\n")

q, t1, t2, t3 = 0, 0, 0, 0

while True:
    if b3 == 0:
        print("\n\nB3 == 0")
        print("\nThus,")
        print(f"GCD({num1}, {num2}) = {a3}")
        print("NO INVERSE")
        exit(0)

    if b3 == 1:
        print("\n\nB3 == 1")
        print("\nThus,")
        print(f"GCD({num1}, {num2}) = B3 = {b3}")
        print(f"MMI of {num1} under {num2} = B2 = {b2}")
        exit(0)

    q = int(a3/b3)
    t1 = a1 - q*b1
    t2 = a2 - q*b2
    t3 = a3 - q*b3
    a1 = b1
    a2 = b2
    a3 = b3
    b1 = t1
    b2 = t2
    b3 = t3
    print(f"\t{q}\t{a1}\t{a2}\t{a3}\t{b1}\t{b2}\t{b3}\t{t1}\t{t2}\t{t3}\n")
