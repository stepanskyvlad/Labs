import math


while True:
    try:
        x = float(input("Enter number x: "))
        y = float(input("Enter number y: "))
    except ValueError as ve:
        print(f"There's an error: {ve}")
    else:
        numerator = 2*x+y*math.cos(x)
        root = y + 4.831
        if root <= 0:
            print("There's the negative root or equal 0")
            continue
        else:
            denominator = math.log(root)
            r = numerator/denominator
            print(f"There's the result: {r}")
            break
