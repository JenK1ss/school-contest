n = int(input())
m = int(input())
while n != m:
    if n > m:
        n = n-m
    elif n < m:
        m = m-n
print(n)
