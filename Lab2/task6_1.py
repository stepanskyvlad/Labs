import math


while True:
    try:
        x = float(input('Enter the number x: '))
        y = float(input('Enter the number y: '))
    except ValueError as ve:
        print('Please, enter numbers')
    else:
        if y < 0:
            print("Enter a positive number 'y'")
            continue
        else:
            numerator = 0.81*math.cos(x)
            denominator = math.log(y)+2*x**3
            if denominator == 0:
                print("We cannot divide by zero. \nEnter other numbers")
            else:
                r = numerator/denominator
                print(f"The result is {r}")
                break
