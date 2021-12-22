from utils import *

# always input in Bin format

def multModulo(inp1, inp2):
    ans = str(decimalToBin((binToDecimal(int(inp1)) * binToDecimal(int(inp2))) % ((2**16) + 1)))
    ans = f"{'0'*(16 - len(ans))}{ans}"
    return ans

def addModulo(inp1, inp2):
    ans = str(decimalToBin((binToDecimal(int(inp1)) + binToDecimal(int(inp2))) % (2**16)))
    ans = f"{'0'*(16 - len(ans))}{ans}"
    return ans

def oddRound(inp_blocks, subkeys):
    p1 = inp_blocks[0]
    p2 = inp_blocks[1]
    p3 = inp_blocks[2]
    p4 = inp_blocks[3]
    k1 = subkeys[0]
    k2 = subkeys[1]
    k3 = subkeys[2]
    k4 = subkeys[3]

    p1 = multModulo(p1, k1)
    p2 = addModulo(p3, k3)
    p3 = addModulo(p2, k2)
    p4 = multModulo(p4, k4)

    return [p1, p2, p3, p4]


def evenRound(inp_blocks, subkeys):
    p1 = inp_blocks[0]
    p2 = inp_blocks[1]
    p3 = inp_blocks[2]
    p4 = inp_blocks[3]
    k5 = subkeys[0]
    k6 = subkeys[1]

    q1 = binXor(p1, p2)
    q2 = binXor(p3, p4)

    q3 = multModulo(addModulo(multModulo(k5, q1), q2), k6)
    q4 = addModulo(multModulo(k5, q1), q3)

    p1 = binXor(p1, q3)
    p2 = binXor(p2, q3)
    p3 = binXor(p3, q4)
    p4 = binXor(p4, q4)

    return [p1, p2, p3, p4]

def outputTransformation(inp_blocks, subkeys):
    p1 = inp_blocks[0]
    p2 = inp_blocks[1]
    p3 = inp_blocks[2]
    p4 = inp_blocks[3]
    k49 = subkeys[0]
    k50 = subkeys[1]
    k51 = subkeys[2]
    k52 = subkeys[3]

    c1 = multModulo(p1, k49)
    c2 = addModulo(p2, k50)
    c3 = addModulo(p3, k51)
    c4 = multModulo(p4, k52)

    print("\n\nFINAL OUTPUT")
    print(f"\nC1 = {formatBin(c1)}")
    print(f"\nC2 = {formatBin(c2)}")
    print(f"\nC3 = {formatBin(c3)}")
    print(f"\nC4 = {formatBin(c4)}")

    return [c1, c2, c3, c4]
