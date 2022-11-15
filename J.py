a = int(input())
b = 0
count = 0
while a != 0:
    b += a
    a = int(input())
    count += 1
print(round(b/count,2))
