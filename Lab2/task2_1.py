import math


def calculate(x, y):
    try:
        x = float(x)
        y = float(y)
        denominator = math.cos(2 * y)
        numerator = 3.5 * x + 1
        r = math.log(x) + (numerator / denominator)
    except ValueError as ve:
        print(f"There is an error {ve}")
    except ZeroDivisionError as zd:
        print(f"There is an error {zd}")
    except TypeError as te:
        print(f"There is an error {te}")
    else:
        print(f"Result is {r}")


a = input("Enter number 'x': ")
b = input("Enter number 'y': ")
calculate(a, b)
