n = int(input())
name = input()
#monkey = 90 parrot = 10 elephant = 300
if name == 'monkey':
    n = n//90
    if n == 0:
        print(1)
    else:
        print(n)
elif name == 'parrot':
    n = n//10
    if n == 0:
        print(1)
    else:
        print(n)
elif name == 'elephant':
    n = n//300
    if n == 0:
        print(1)
    else:
        print(n)
