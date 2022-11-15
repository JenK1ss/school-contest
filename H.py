n = int(input())
for i in range(0,n//2+1):
    if 2**i == n:
        flag = 'YES'
        break
    else:
        flag = 'NO'
print(flag)
