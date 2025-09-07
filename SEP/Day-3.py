def print_something(n):
    if n == 0:
        return
    print("Hello, world!")
    print_something(n - 1)

print_something(5)