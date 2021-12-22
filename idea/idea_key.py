from utils import *

def dispSubkeys(s_index, subkeys):
    for i in range(s_index, len(subkeys)):
        print(f"\nK{i+1} = {formatBin(subkeys[i])}")


# input always in Bin format
def genSubkeys(key):

    if not len(key) == 64:
        print("INVALID INPUT")
        exit(0)

    print("\n\nKEY EXPANSION")

    subkeys = []
    subkeys.extend(makeGroups(key, 16))
    dispSubkeys(0, subkeys)

    for i in range(12):
        key = l_shift(key, 25)
        print("\n\nLEFT SHIFT OPERATION | Number of bits = 25")
        print(f"\nKey = {formatBin(key)}")
        subkeys.extend(makeGroups(key, 16))
        dispSubkeys(4*(i+1), subkeys)

    return subkeys


def main():
    key = input("key (in Hex format) = ")
    key = hexToBin(key)
    subkeys = genSubkeys(key)


if __name__ == "__main__":
    main()
