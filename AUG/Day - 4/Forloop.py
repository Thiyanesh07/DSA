# second largest element in an array using a for loop

arr = [12, 45, 23, 67, 89, 34, 67]
largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Array:", arr)
print("Second Largest Element:", second_largest)
