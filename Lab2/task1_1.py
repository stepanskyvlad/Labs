import math


while True:
    try:
        x = float(input('Enter number X: '))
        y = float(input('Enter number Y: '))
    except ValueError as ve:
        print(f"An error {ve}. Please, try again")
    else:
        if (2 * x) > 709:
            print(f"Enter a smaller number x: ")
            continue
        else:
            numerator = math.exp(2 * x) + math.sin(y)
            number = 3.8 * x + y
            if number > 0:
                denominator = math.log(number)
                if denominator < 0:
                    print("Не можна ділити на нуль")
                else:
                    R = numerator / denominator
                    print(f"Результат --> {R}")
                    break
            else:
                print("В логарифмі число менше за нуль")
