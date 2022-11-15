max1 = 0
min1 = 0
max2 = 0
min2 = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a > 0:
        if a > max1:
            max2 = max1
            max1 = a
        elif a > max2:
            max2 = a
    elif a < 0:
        if a < min1:
            min2 = min1
            min1 = a
        elif a < min2:
            min2 = a
max_pr = max(max1 * max2, min1 * min2, max1 * min1)
print(max_pr)
