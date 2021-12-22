from utils import *
from single_sbox import performSbox
from aes_tables import *

# Round starts from 0

# input always in Hex format
def genKey(round_key, round_num):
    round_key = round_key.replace(" ", "")

    if not len(round_key) == 32:
        print("INVALID INPUT")

    w0 = round_key[:8]
    w1 = round_key[8:16]
    w2 = round_key[16:24]
    w3 = round_key[24:]

    print(f"\nYOUR ROUND {round_num} KEYS\n")
    print(formatHex(w0))
    print(formatHex(w1))
    print(formatHex(w2))
    print(formatHex(w3))

    temp = w3
    print(f"\ntemp = {formatHex(temp)}")
    temp = formatHex(temp).split()
    harsh = temp[0]
    temp = temp[1:]
    temp.append(harsh)
    print("\n1 BYTE LEFT CIRCULAR SHIFT")
    print(f"{' '.join(temp)}")

    new_word = []
    for group in temp:
        print(f"\n{group}\n")
        new_word.append(performSbox(group))
    
    temp = hexToBin("".join(new_word))
    print("\n\nS-BOX SUBSTITUTION")
    print(f"\n{formatBin(temp)}")
    round_const = round_constants[round_num]
    round_const += "000000"
    print(f"\n\nRound constant = {round_const}")
    round_const = hexToBin(round_const)
    print(f"Round constant in Bin = {formatBin(round_const)}")
    
    g = binXor(temp, round_const)

    print("\n\nXOR WITH ROUND CONSTANT")
    print(f"\n{formatBin(g)}")
    print(f"\ng = {formatHex(binToHex(g))}")

    print("\n\nFINAL XOR OPERATIONS")

    w0 = hexToBin(w0)
    w1 = hexToBin(w1)
    w2 = hexToBin(w2)
    w3 = hexToBin(w3)
    
    print("\ng XOR w0")
    print(formatBin(g))
    print(formatBin(w0))
    w4 = binXor(g, w0)
    print(f"\nw4 = {formatBin(w4)} = {formatHex(binToHex(w4))}")

    print("\nw4 XOR w1")
    print(formatBin(w4))
    print(formatBin(w1))
    w5 = binXor(w4, w1)
    print(f"\nw5 = {formatBin(w5)} = {formatHex(binToHex(w5))}")

    print("\nw5 XOR w2")
    print(formatBin(w5))
    print(formatBin(w2))
    w6 = binXor(w5, w2)
    print(f"\nw6 = {formatBin(w6)} = {formatHex(binToHex(w6))}")

    print("\nw6 XOR w3")
    print(formatBin(w6))
    print(formatBin(w3))
    w7 = binXor(w6, w3)
    print(f"\nw7 = {formatBin(w7)} = {formatHex(binToHex(w7))}")

genKey("EAD27321 B58DBAD2 312BF560 7F8D292F", 0)