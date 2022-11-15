b = []
a = int(input())
a = ([int(i) for i in str(a)])
if a == 1:
    print('1')
else:
    while len(a) > 0:
        b.append(min(a))
        a.remove(min(a))
i = 0
while b[i] == 0:
    i += 1
b[0], b[i] = b[i], b[0]
print(*b, sep='')

