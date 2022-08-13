while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a < b:
        break
    print("The first number is greater than the second. \nPlease, try again")

my_list = [i for i in range(a, b+1)]
print(my_list)
print(f"The amount of the numbers is {len(my_list)}")
