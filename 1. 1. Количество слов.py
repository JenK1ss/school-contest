a = input()
a = a.lower().split()
res = []
for word in a:
    if word in res:
        pass
    else:
        res.append(word)
print(len(res))
