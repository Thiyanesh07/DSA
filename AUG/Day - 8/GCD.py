n = int(input())
m = int(input())

for i in range(min(n,m),0,-1):
    if n%i==0 and m%i==0:
        print(i)
        break