import math


while True:
    try:
        x = float(input("Enter number x: "))
        y = float(input("Enter number y: "))
    except ValueError as ve:
        print(f"There's an error: {ve}")
    else:
        numerator = 2.37*math.sin(x+1)
        root = 4*y**2-0.1*y+5
        if root < 0:
            print("There's the negative root")
            continue
        else:
            denominator = math.sqrt(root)
            r = numerator/denominator
            print(f"The result is {r}")
            break
