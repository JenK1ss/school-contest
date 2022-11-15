a = int(input())
count = 0
while a != 0:
    if a % 2 == 0:
        if a>count:
            count = a
    a = int(input())
print(count)
