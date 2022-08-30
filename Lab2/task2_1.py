import math


def calculate_func(x, y):
    try:
        x = float(x)
        y = float(y)
        denominator = math.cos(2 * y)
        numerator = 3.5 * x + 1
        r = math.log(x) + (numerator / denominator)
    except ValueError as ve:
        print(f"There is an error - {ve}")
    except ZeroDivisionError as zd:
        print(f"There is an error - {zd}")
    except TypeError as te:
        print(f"There is an error - {te}")
    else:
        print(f"Result is {r}")


def user_input():
    while True:
        try:
            x = float(input("Enter number 'x': "))
            y = float(input("Enter number 'y': "))
        except ValueError as ve:
            print(f"There is {ve}. \nPlease, enter your numbers again!")
        else:
            break
    return x, y


def main():
    x, y = user_input()
    calculate_func(x, y)


if __name__ == '__main__':
    main()
