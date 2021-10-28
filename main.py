hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

binary_to_hex = dict()

for key, value in hex_to_binary.items():
    binary_to_hex[value] = key


def rotr(binary, n):
    return binary[len(binary)-n:] + binary[:len(binary)-n]


def shr(binary, n):
    return "0"*n + binary[:len(binary)-n]


def hexToBinary(hex):
    binary = ""
    for ch in hex:
        binary += hex_to_binary[ch]
    return binary


def addSpacing(binary):
    count = 0
    temp = ""
    for ch in binary:
        temp += ch
        count += 1
        if count % 4 == 0:
            temp += " "
    return temp


def xor(*args):
    temp = ""
    for count in range(len(args[0])):
        one_count = 0
        for binary in args:
            if binary[count] == "1":
                one_count += 1
        if one_count % 2 == 0:
            temp += "0"
        else:
            temp += "1"

    return temp


def sigma0512(input):
    binary = hexToBinary(input)
    rotr28 = rotr(binary, 28)
    rotr34 = rotr(binary, 34)
    rotr39 = rotr(binary, 39)

    print(f"ROTR28 value = {addSpacing(rotr28)}")
    print(f"ROTR34 value = {addSpacing(rotr34)}")
    print(f"ROTR39 value = {addSpacing(rotr39)}")

    print(f"sigma value = {addSpacing(xor(rotr28, rotr34, rotr39))}")


def sigma1512(input):
    binary = hexToBinary(input)
    rotr14 = rotr(binary, 14)
    rotr18 = rotr(binary, 18)
    rotr41 = rotr(binary, 41)

    print(f"ROTR14 value = {addSpacing(rotr14)}")
    print(f"ROTR18 value = {addSpacing(rotr18)}")
    print(f"ROTR41 value = {addSpacing(rotr41)}")

    print(f"sigma value = {addSpacing(xor(rotr14, rotr18, rotr41))}")


def sd0512(input):
    binary = hexToBinary(input)
    rotr1 = rotr(binary, 1)
    rotr8 = rotr(binary, 8)
    shr7 = shr(binary, 7)

    print(f"ROTR1 value = {addSpacing(rotr1)}")
    print(f"ROTR8 value = {addSpacing(rotr8)}")
    print(f"SHR7 value = {addSpacing(shr7)}")

    print(f"sd value = {addSpacing(xor(rotr1, rotr8, shr7))}")


def sd0512(input):
    binary = hexToBinary(input)
    rotr19 = rotr(binary, 19)
    rotr61 = rotr(binary, 61)
    shr6 = shr(binary, 6)

    print(f"ROTR19 value = {addSpacing(rotr19)}")
    print(f"ROTR61 value = {addSpacing(rotr61)}")
    print(f"SHR6 value = {addSpacing(shr6)}")

    print(f"sd value = {addSpacing(xor(rotr19, rotr61, shr6))}")


def main():
    print("Choose an option")
    functions = ["sigma0512", "sigma1512", "sd0512", "sd1512"]
    for index, function in enumerate(functions):
        print(f"{index+1}. {function}")

    choice = "temp"
    while not (choice.isnumeric() and int(choice) in range(1, 5)):
        choice = input("\nEnter your choice: ")
    choice = int(choice)

    hex = input("Enter hexadecimal value: ")
    func = eval(functions[choice-1])
    func(hex)


# sigma0512("ABCDEF0123456789")

if __name__ == "__main__":
    main()
