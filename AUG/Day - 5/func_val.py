# sum of even numbers in array

def sum_even(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total  

nums = [5, 6, 7, 8, 10]
result = sum_even(nums)
print("Array :", nums)
print("Sum of even numbers:", result)