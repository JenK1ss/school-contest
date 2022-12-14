a = list(map(str,input().split()))
b = []
count = []
a.sort()
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            b.append(a[i])
            count.append(a.count(a[i]))
ans = dict(zip(b,count))
sorted_dict = {}
sorted_keys = reversed(sorted(ans, key=ans.get))

for w in sorted_keys:
    sorted_dict[w] = ans[w]

print(sorted_dict)

