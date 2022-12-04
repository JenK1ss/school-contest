n, mid = map(int,input().split())
prodano = []
popdesh = []
popdor = []
for i in range(n):
    tovar,status = map(int,input().split())
    if status == 1:
        prodano.append(tovar)
for desh in prodano:
    if desh < mid:
        popdesh.append(desh)
for dor in prodano:
    if dor > mid:
        popdor.append(dor)
print(sum(popdesh+popdor),n - len(prodano), end='.')
