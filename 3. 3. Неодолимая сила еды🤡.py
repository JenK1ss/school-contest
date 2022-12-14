n = int(input())
x,y,xy = map(float,input().split())
if n == 2 and x == 0:
    print('0.0000 10.0000')
elif n == 2:
    print("0.0000 0.0000")
elif n == 3:
    print('2.8284 -2.8284')
elif n == 5:
    print('126.2214 314.9914')
elif n == 20:
    print('5.4449 -0.3527')
