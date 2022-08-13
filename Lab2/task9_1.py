import math


while True:
    try:
        x = float(input("Enter number x: "))
        y = float(input("Enter number y: "))
    except ValueError as ve:
        print(f"There's an error: {ve}")
    else:
        numerator = (2*x+y)**3
        root = y+0.75
        if root < 0 or root == 1:
            print("There's the negative root or equal 1")
            continue
        else:
            denominator = math.log(root)
            r = numerator/denominator
            print(f"There's the result: {r}")
            break
