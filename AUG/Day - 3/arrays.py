# Rotate an array to the left by 'k' positions

def left_rotate(arr, k):
    n = len(arr)
    k = k % n  
    return arr[k:] + arr[:k]


arr = [10, 20, 30, 40, 50]
k = 2

print("Original Array:", arr)
rotated = left_rotate(arr, k)
print(f"Array after {k} left rotations:", rotated)
