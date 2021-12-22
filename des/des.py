from utils import *
from des_tables import *

# input always in bin format


def keyRound(inp, round_num):
    c0 = inp[:28]
    d0 = inp[28:]

    print(f"\n\nRound {round_num+1} | 28 + 28 = 56\n")
    print(f"Co = {formatBin(c0)}")
    print(f"Do = {formatBin(d0)}")

    c1 = l_shift(c0, num_shifts[round_num])
    d1 = l_shift(d0, num_shifts[round_num])

    print(
        f"\n\nLEFT CIRCULAR SHIFT | Number of bits rotated = {num_shifts[round_num]}\n")
    print(f"C1 = {formatBin(c1)}")
    print(f"D1 = {formatBin(d1)}")

    temp = c1+d1
    ans = subs(temp, permuted_choice2)

    print("\n\nPERMUTED CHOICE-2 | 56 -> 48\n")
    print(f"PC2(C1D1) = {formatBin(ans)}")
    print(f"Thus subkey for Round {round_num+1} = {formatHex(binToHex(ans))}")

    return [temp, ans]


# input always in bin format
def permutedChoice1(key):
    return subs(key, permuted_choice1)


# input always in Hex
def genKey(key):
    if not len(key) == 16:
        print("INVALID INPUT | genKey (For Bin input -> remove key = hexToBin(key) line)")
        exit(0)

    key = hexToBin(key)
    pc2 = permutedChoice1(key)

    print("\n\nKEY EXPANSION PROCESS")
    print("\n\nPERMUTED CHOICE-1 | 64 -> 56\n")
    print(f"PC1(key) = {formatBin(pc2)}")

    subkeys = []
    ans = pc2
    for round in range(16):
        temp = keyRound(ans, round)
        ans = temp[0]
        subkeys.append(temp[1])

    return subkeys


# genKey("13579BDF02468ACE")


# input always in bin format
def initPermutation(inp):
    return subs(inp, init_permutation)


def sbox(inp, sbox_num):
    if not len(inp) == 6:
        print("INVALID INPUT | sbox")
        exit(0)

    row = binToDecimal(int(inp[0] + inp[-1]))
    column = binToDecimal(int(inp[1:-1]))
    temp = s_box[sbox_num][row][column]
    temp = decimalToBin(temp)
    ans = f"{'0'*(4-len(temp))}{temp}"

    print(f"S-BOX - {sbox_num+1}\n")
    print(f"outer 2 bits = {inp[0] + inp[-1]} = {row} (row no)")
    print(f"inner 4 bits = {inp[1:-1]} = {column} (column no)")
    print(f"Thus, S{sbox_num+1} = {ans}")
    print()

    return ans

# Round number - start from 0

# input always in bin format
def round(inp, round_num, subkey):
    l0 = inp[:32]
    r0 = inp[32:]

    print(f"\n\nRound {round_num+1}\n")
    print(f"Lo = {formatBin(l0)}")
    print(f"Ro = {formatBin(r0)}")

    er0 = subs(r0, expansion)

    print("\n\nAPPLY EXPANSION TABLE | 32 -> 48\n")
    print(f"E(Ro) = {formatBin(er0)}")

    xor_out = binXor(er0, subkey)

    print(f"\nK{round_num+1} XOR E(Ro) = {formatBin(xor_out)}\n")

    groups = []
    count = 0
    group = ""
    for ch in xor_out:
        count += 1
        group += ch
        if count == 6:
            count = 0
            groups.append(group)
            group = ""

    sbox_out = ""
    for i in range(8):
        sbox_out += sbox(groups[i], i)
    print(f"Thus, S-boxes output = {formatBin(sbox_out)}")

    permutation_out = subs(sbox_out, permutation)

    print("\n\nPERMUTATION | 32 -> 32\n")
    print(f"P(S-boxes output) = {formatBin(permutation_out)}")

    r1 = binXor(l0, permutation_out)
    print("\n\nXOR OPERATION\n")
    print(f"Lo XOR p(S-box output) = {formatBin(r1)}")
    l1 = r0

    print()
    print(f"L1 = {formatBin(l1)}")
    print(f"R1 = {formatBin(r1)}")

    print(f"\nThus, Round {round_num+1} output = {formatBin(l1+r1)}")


round("1100110000000000110011001111111111110000101010101111000010101010",
      0, "000110110000001011101111111111000111000001110010")

def main():
    pass


if __name__ == "__main__":
    main()
