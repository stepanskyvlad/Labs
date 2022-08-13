import math

while True:
    try:
        x = float(input("Enter number 'x': "))
        y = float(input("Enter number 'y': "))
    except ValueError as ve:
        print(f"There is an error {ve}")
    else:
        denominator = math.cos(2 * y)
        numerator = 3.5*x+1
        if x > 0 and denominator != 0:
            R = math.log(x) + (numerator/denominator)
            print(f"Result is {R}")
            break
        print("X and denominator can't be equal to 0")

while True:
    try:
        x = float(input("Enter number 'x': "))
        y = float(input("Enter number 'y': "))
        denominator = math.sin(2 * y)
        numerator = 3.5 * x + 1
        R = math.log(x) + (numerator / denominator)
    except ValueError as ve:
        print(f"There is an error: {ve}")
    except ZeroDivisionError as zd:
        print(f"There is an error: {zd}")
    else:
        print(f"Result is {R}")
        break

