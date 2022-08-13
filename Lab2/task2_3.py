while True:
    try:
        n = int(input("Enter a number greater then zero: "))
    except ValueError as ve:
        print(f"There's an error: {ve}")
    else:
        my_list = range(1, n+1)
        result = 1
        for i in my_list:
            result *= i
        print(f"The result is {result}")
        break
