import random


number = int(input("Enter a number of integers --> "))
my_list = random.sample(range(10, 100), number)
sum_of_list = sum(my_list)
print(f"Your list:\n{my_list}\nThe sum of the list --> {sum_of_list}")
if len(my_list) % 2 == 0:
    my_list.insert(round(len(my_list)/2), sum_of_list)
else:
    my_list.append(sum_of_list)
print(my_list)
