x, p, y = map(int,input().split())
x *= 100
y *= 100
count = 0
while x < y:
    x += x*(p/100)
    x = x//1
    count += 1
print(count)
