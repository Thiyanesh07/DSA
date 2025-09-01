n = int(input())

c = n
rev = 0


while c > 0:
    rem = c % 10
    rev = rev * 10 + rem

print(rev)




