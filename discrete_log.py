def modInverse(num, m):
    for x in range(1, m):
        if (((num % m) * (x % m)) % m == 1):
            return x
    return -1


def add(point1, point2, a, prime):
    if point1[0] == point2[0] and point1[1] == point2[1]:
        num = 3 * (point1[0]**2) + a
        denom = 2 * point1[1]
    else:
        num = point2[1] - point1[1]
        denom = point2[0] - point1[0]

    temp = modInverse(denom, prime)
    if temp == -1:
        print("INVALID")
        print("modInverse NOT POSSIBLE")
        exit(0)

    print(f"\n\nNumerator = {num}")
    print(f"Denominator = {denom}")
    print(f"modInverse of {denom} under {prime} = {temp}")

    temp *= num
    print(f"New Numerator = {temp}")
    lambda_val = temp % prime
    print(f"Lambda value = {lambda_val}")

    ans = []
    ans.append(((lambda_val**2) - point1[0] - point2[0]) % prime)
    ans.append((lambda_val * (point1[0] - ans[0]) - point1[1]) % prime)

    return ans


def main():
    prime = int(input("p = "))
    a = int(input("a = "))
    b = int(input("b = "))

    point1 = [int(num) for num in input(
        "\nCoordinates of point1 separated by space = ").split()]
    point2 = [int(num) for num in input(
        "\nCoordinates of point2 separated by space = ").split()]

    attempts = int(input("\nnumber of attempts = "))

    ans = add(point1, point1, a, prime)
    for i in range(attempts):
        print(ans)
        if ans == point2:
            print("\n\nFOUND")
            print(f"Your key is {i+2}")
            exit(0)
        ans = add(ans, point1, a, prime)

    print("\n\nNOT FOUND")


if __name__ == "__main__":
    main()
