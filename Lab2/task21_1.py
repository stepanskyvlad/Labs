import math

x = float(input("Введіть X: "))
y = float(input("Введіть Y: "))
z = float(input("Введіть Z: "))
a = float(input("Введіть A: "))
b = float(input("Введіть B: "))
while True:
    if a - b ** 3 == 0:
        print("На нуль ділити не можна")
        a = float(input("Введіть A: "))
        b = float(input("Введіть B: "))
    else:
        denominator = a - b ** 3
        break

while True:
    if x + 2.6 * y * math.sin(z) < 0:
        print("Під квадратним коренем число менше нуля \nСпробуйте ввести інші числа:")
        x = float(input("Введіть X: "))
        y = float(input("Введіть Y: "))
        z = float(input("Введіть Z: "))
    else:
        F = math.sqrt(x + 2.6 * y * math.sin(z)) / denominator
        print(f"Результат обчислень: {F}")
        break
