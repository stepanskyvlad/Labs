import math


# solve this function without any errors
def calculate_func(x, y):
    result = (math.exp(2 * x) + math.sin(y)) / (math.log(3.8 * x + y))
    return result


def get_numbers():
    while True:
        try:
            x = float(input('Enter number X: '))
            y = float(input('Enter number Y: '))
        except ValueError as ve:
            print(f"An error - {ve}. Please, try again")
        else:
            break
    return x, y


def save_calculate(func):
    def save_version(x, y):
        if (2 * x) > 709:
            print(f"Enter a smaller number x")
            return
        elif 3.8 * x + y < 0:
            print("There's the number less than zero in the logarithm")
            return
        elif math.log(3.8 * x + y) < 0:
            print("The denominator is less than zero")
            return
        return func(x, y)

    return save_version


def main():
    calculate_safe = save_calculate(calculate_func)
    x, y = get_numbers()
    print(calculate_safe(x, y))


if "__main__" == __name__:
    main()
