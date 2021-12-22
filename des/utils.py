hex_to_bin = {
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


def hexToBin(hex):
    bin = ""
    for ch in hex:
        bin += hex_to_bin[ch]
    return bin


bin_to_hex = dict()

for key, value in hex_to_bin.items():
    bin_to_hex[value] = key


def binToHex(bin):
    if not len(bin) % 4 == 0:
        print("INVALID INPUT | binToHex")
        exit(0)
    hex = ""
    groups = []
    count = 0
    group = ""
    for ch in bin:
        count += 1
        group += ch
        if count == 4:
            count = 0
            groups.append(group)
            group = ""

    for group in groups:
        hex += bin_to_hex[group]

    return hex


def formatBin(bin):
    groups = []
    count = 0
    group = ""
    for ch in bin:
        count += 1
        group += ch
        if count == 4:
            count = 0
            groups.append(group)
            group = ""
    if group:
        groups.append(group)

    return " ".join(groups)


def formatHex(hex):

    groups = []
    count = 0
    group = ""
    for ch in hex:
        count += 1
        group += ch
        if count == 2:
            count = 0
            groups.append(group)
            group = ""
    if group:
        groups.append(group)

    return " ".join(groups)


def l_shift(inp, num_bits):
    return inp[num_bits:] + inp[:num_bits]


def subs(inp, mat):
    ans = ""
    for index in mat:
        ans += inp[index-1]
    return ans


def binXor(inp1, inp2):
    if not len(inp1) == len(inp2):
        print("INVALID INPUT | XOR")
        exit(0)

    ans = ""
    for i in range(len(inp1)):
        if inp1[i] == inp2[i]:
            ans += "0"
        else:
            ans += "1"
    return ans


def binAnd(inp1, inp2):
    if not len(inp1) == len(inp2):
        print("INVALID INPUT | AND")
        exit(0)

    ans = ""
    for i in range(len(inp1)):
        if inp1[i] == "1" and inp2[i] == "1":
            ans += "1"
        else:
            ans += "0"
    return ans


def binOr(inp1, inp2):
    if not len(inp1) == len(inp2):
        print("INVALID INPUT | OR")
        exit(0)

    ans = ""
    for i in range(len(inp1)):
        if inp1[i] == "0" and inp2[i] == "0":
            ans += "0"
        else:
            ans += "1"
    return ans


def binNot(inp):

    ans = ""
    for ch in inp:
        if ch == "0":
            ans += "1"
        else:
            ans += "0"
    return ans


def binToDecimal(bin):

    bin1 = bin
    decimal, i, n = 0, 0, 0
    while(bin != 0):
        dec = bin % 10
        decimal = decimal + dec * pow(2, i)
        bin = bin//10
        i += 1
    return decimal


def decimalToBin(n):
    return bin(n).replace("0b", "")


def makeGroups(inp, group_len):
    groups = []
    count = 0
    group = ""
    for ch in inp:
        count += 1
        group += ch
        if count == group_len:
            count = 0
            groups.append(group)
            group = ""

    if group:
        print("\n\nNON-UNIFORM GROUP")
        groups.append(group)

    return groups
