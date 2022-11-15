n = int(input())
s = input()
a = [int(n) for n in s.split()]

print(min(a), a.count(min(a)))
