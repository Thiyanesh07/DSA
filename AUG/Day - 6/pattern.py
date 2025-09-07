n = 7
c = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(c**2, end=' ')
        c += 1
    print()