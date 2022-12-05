try:
    a,d,b = map(str,input().split())
    a = int(a)
    b = int(b)
except:
    print('Bad input')
else:
    if d == '+':
        print(a+b)
    elif d == '-':
        print(a-b)
    elif d == '*':
        print(a*b)
    elif d == '^':
        print(a**b)
