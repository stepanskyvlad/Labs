import math


while True:
    try:
        x = float(input("Enter number x: "))
        y = float(input("Enter number y: "))
    except ValueError as ve:
        print(f"There is an error: {ve}")
    else:
        if x < 0 or y < 0:
            print('Enter other numbers')
            continue
        else:
            numerator = 9.33*x**3+math.sqrt(x)
            denominator = math.log(y+3.5)+math.sqrt(y)
            r = numerator/denominator
            print(f"The result is {r}")
            break
