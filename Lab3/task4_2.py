user_input = input("Enter your string: ")


def change_line(user_str):
    first_half = bytearray(user_str[:round(len(user_str)/2)], 'utf-8').replace(b':', b'.')
    second_half = bytearray(user_str[round(len(user_str)/2):], 'utf-8').replace(b'!', b'.')
    changed_line = (first_half+second_half).decode('utf-8')
    return changed_line


def print_result():
    changed_line = change_line(user_input)
    print(f"Your result is: \n{changed_line}")


def main():
    change_line(user_input)
    print_result()


if '__main__' == __name__:
    main()
