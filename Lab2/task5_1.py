import math


while True:
    try:
        x = float(input('Enter number x: '))
        y = float(input('Enter number y: '))
        z = float(input('Enter number z: '))
    except ValueError as ve:
        print(f"There's an error: {ve} \nPlease, enter numbers")
    else:
        numerator = 7.8*x**2+3.52*y
        if (x+2*z) < 0 or z > 709 or math.log(x+2*z)+math.exp(z) == 0:
            print('Enter other numbers')
            continue
        else:
            denominator = math.log(x+2*z)+math.exp(z)
            r = numerator/denominator
            print(f"The result is: {r}")
            break
