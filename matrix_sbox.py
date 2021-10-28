from aes_sbox import sbox, inv_sbox


def performSbox(hex):
    row = hex[0]
    row = eval(f"0x{row}")
    column = hex[1]
    column = eval(f"0x{column}")
    return sbox[row][column]


def performInvSbox(hex):
    row = hex[0]
    row = eval(f"0x{row}")
    column = hex[1]
    column = eval(f"0x{column}")
    return inv_sbox[row][column]


print("Choose an option")
functions = ["performSbox", "performInvSbox"]
for index, function in enumerate(functions):
    print(f"{index+1}. {function}")

choice = "temp"
while not (choice.isnumeric() and int(choice) in range(1, 3)):
    choice = input("\nEnter your choice: ")
choice = int(choice)
func = eval(functions[choice-1])

row1 = input("Enter row1: ").split()
row2 = input("Enter row2: ").split()
row3 = input("Enter row3: ").split()
row4 = input("Enter row4: ").split()

matrix = [row1, row2, row3, row4]

for row in matrix:
    temp = ""
    for column in row:
        temp += func(column) + " "
    print(temp)
