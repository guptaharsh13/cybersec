from aes_tables import *
from utils import *


def performSbox(hex):
    binary = hexToBin(hex)
    print(f"Bin values = {binary[:4]} {binary[4:]}")
    row = hex[0]
    print(f"Row = {row}")
    row = eval(f"0x{row}")
    column = hex[1]
    print(f"Column = {column}")
    column = eval(f"0x{column}")
    ans = sbox[row][column]
    print(f"value from sbox = {ans}")
    return ans


def performInvSbox(hex):
    binary = hexToBin(hex)
    print(f"Bin values = {binary[:4]} {binary[4:]}")
    row = hex[0]
    print(f"Row = {row}")
    row = eval(f"0x{row}")
    column = hex[1]
    print(f"Column = {column}")
    column = eval(f"0x{column}")
    print(f"value from inverse sbox = {inv_sbox[row][column]}")


def main():
    print("Choose an option")
    functions = ["performSbox", "performInvSbox"]
    for index, function in enumerate(functions):
        print(f"{index+1}. {function}")

    choice = "temp"
    while not (choice.isnumeric() and int(choice) in range(1, 3)):
        choice = input("\nEnter your choice\n")
    choice = int(choice)

    hex = input("Enter only 2 bit hex value\n")
    print("\n")
    func = eval(functions[choice-1])
    func(hex)


if __name__ == "__main__":
    main()
