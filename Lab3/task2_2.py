def get_decimal_num():
    while True:
        x = 0
        binary = input("Enter your binary number: ")
        for i in binary:
            if i != '1' and i != '0':
                x += 1
        if x == 0:
            print(f"{binary} is a binary number.")
            break
        else:
            print(f"Please, try again.")
            continue
    return binary


def get_decimal(num):
    decimal_number = int(num, 2)
    return decimal_number


def main():
    binary_num = get_decimal_num()
    decimal_num = get_decimal(binary_num)
    print(f"Your binary number in decimal system is {decimal_num}")


if __name__ == '__main__':
    main()
    