num = int(input("num = "))
print()
print("Powers", end="\t")

for i in range(1, num):
    print(i, end="\t")

print("\nNumbers")

roots = []

for i in range(1, num):
    print(i, end="\t")
    temp = set()
    for j in range(1, num):
        power = (i**j) % num
        temp.add(power)
        print(power, end="\t")
    if len(temp) == num-1:
        roots.append(i)
    print()

print(
    f"\nThus, primitive roots of {num} are {'none' if len(roots) == 0 else ', '.join([str(num) for num in roots])}")
