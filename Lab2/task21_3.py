import math

number = 0
while number < 100:
    number = int(input('Введіть натуральне число більше 100: '))

# Сформовуємо послідовність від 10 до N
numbers = [n for n in range(10, number + 1)]

# Виводимо в друк натуральні числа, як квадрат числа і корінь числа
for a in numbers:
    if a % math.sqrt(a) == 0:
        b = math.sqrt(a)
        print(f"Квадрат числа {a} - корінь {b}")
    else:
        continue

# Виводимо в друк натуральні числа, як куб числа і корінь числа
for a1 in numbers:
    if a1 % round(a1 ** (1 / 3.), 3) == 0:
        b1 = round(a1 ** (1 / 3.), 3)
        print(f"Куб числа {a1} - корінь {b1}")
    else:
        continue
