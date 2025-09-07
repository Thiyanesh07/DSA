def print_divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


n = int(input("Enter a number: "))
print_divisors(n)