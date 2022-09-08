def get_number_a():
    while True:
        try:
            a = float(input("Enter a real number greater than 1: "))
            if not a > 1:
                continue
        except ValueError as ve:
            print(f"There's a problem - {ve}")
        else:
            break
    return a
# solving of the func using recursion, but "n" can't be greater than 996
# def solve_func(n):
#     if n == 1:
#         return 1
#     return 1/n + solve_func(n-1)

# solving this task in one loop is better solution
# for performance of this program
# def solve_func(n):
#     s = 0
#     for i in (range(1, n+1)):
#         s += 1/i
#     return s


# In my opinion, to improve this program we should
# use multiprocessing or multithreading
def main():
    a = get_number_a()
    n = 1
    s = 0
    while True:
        s += 1/n
        if s > a:
            break
        n += 1
    print(f"The result of the function is {s:.10f}\n"
          f"The smallest integer is {n}")


if __name__ == "__main__":
    main()
