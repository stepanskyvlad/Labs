import math


while True:
    try:
        x = float(input("Enter the first number 'x': "))
        y = float(input("Enter the second number 'y': "))
        r = (math.log(x-y)+y**4)/(math.exp(y)+2.355*x**2)
    except ValueError as ve:
        print(f"There's an error: {ve} \nPlease, try again")
    except ZeroDivisionError as ze:
        print(f"There's an error: {ze} \nPlease, try again")
    else:
        print(f"Your result is {r}")
        break
