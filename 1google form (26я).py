n, mid = map(int,input().split())
prodano = []
desh = []
dor = []
for i in range(n):
    tovar,status = map(int,input().split())
    if status == 1:
        prodano.append(tovar)
for perebor in prodano:
    if perebor < mid:
        desh.append(perebor)
    else:
        dor.append(perebor)
mpdor = int(max(set(dor), key=dor.count))
mpdesh = int(max(set(desh), key=desh.count))
print(mpdesh*desh.count(mpdesh) + mpdor*dor.count(mpdor), n - len(prodano), end='.')
