a = list(map(str,input().split()))

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            print(a[i],a.count(a[i]))
