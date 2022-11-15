def maks_uniq(a):
    b = []
    for i in a:
        if a.count(i) == 1:
            b.append(i)
    print(max(b))
a = list(map(int,input().split()))
maks_uniq(a)
