# armstrong number check

n = int(input())
temp = n
sum = 0

l = len(str(n))

while n > 0:
    r = n % 10
    sum = sum + r ** l
    n = n // 10
    
if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")