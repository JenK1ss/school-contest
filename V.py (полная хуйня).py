a = list(map(str,input().split()))
b = []
count = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            b.append(a[i])
            count.append(a.count(a[i]))
ans = dict(zip(b,count))
values = list(ans.values())
ans = list(ans)
for g in range(len(ans)):
    print(values[g],ans[g])
