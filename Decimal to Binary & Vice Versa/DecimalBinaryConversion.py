try:
    menu = int(input("\nChoose an option:\n\n1. Decimal to binary\n2. Binary to decimal\n\nInput your option: "))
    if menu < 1 or menu > 2:
        raise ValueError
    if menu == 1:
        dec = int(input("\nInput your decimal number:\nDecimal: "))
        print("Binary: {}\n".format(bin(dec)[2:]))
    elif menu == 2:
        binary = input("\nInput your binary number:\nBinary: ")
        print("Decimal: {}\n".format(int(binary, 2)))
except ValueError:
    print ("\nPlease choose a valid option!!!\n")