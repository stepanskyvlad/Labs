import math


def calculate_func(x, y):
    result = (math.log(x - y) + y ** 4) / (math.exp(y) + 2.355 * x ** 2)
    return result


def get_number():
    while True:
        try:
            x = float(input("Enter the first number 'x': "))
            y = float(input("Enter the second number 'y': "))
        except ValueError as ve:
            print(f"There's an error: {ve} \nPlease, try again")
        else:
            break
    return x, y


def safe_calculate(func):
    def save_version(x, y):
        if x - y < 0:
            print("There's the number less than zero in the logarithm")
            return
        elif (math.exp(y) + 2.355 * x ** 2) > 0:
            print("Denominator is less than zero")
            return
        return func(x, y)

    return save_version


def main():
    secure_computing = safe_calculate(calculate_func)
    x, y = get_number()
    print(secure_computing(x, y))


if __name__ == '__main__':
    main()
