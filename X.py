def posled_ed(a):
    max1_f = 0
    max1 = 0
    for i in range(1,len(a)):
        if a[i-1] == a[i] == '1':
            max1 += 1
            if max1 > max1_f:
                    max1_f = max1
        elif a[i-1] == '0':
            max1 = 0
    if len(a) == a.count('0'):
        print(0)
    else:
        print(max1_f+1)
a = input()
posled_ed(a)
