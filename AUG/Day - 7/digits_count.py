num = int(input())

d = 0
copy = num

while copy > 0:
    copy //= 10
    d += 1


print(d)