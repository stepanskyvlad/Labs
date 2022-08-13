import math


while True:
    try:
        x = float(input("Enter number x: "))
        y = float(input("Enter number y: "))
    except ValueError as ve:
        print(f"There's an error: {ve}")
    else:
        numerator = x**2+2.8*x+0.355
        denominator = math.cos(2*y)+3.6
        if denominator == 0:
            print("There's a division by zero")
            continue
        else:
            r = numerator/denominator
            print(f"The result is {r}")
            break
