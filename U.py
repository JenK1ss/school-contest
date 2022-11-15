number = input()
s = str(number)
if '.' not in s:
    print(int(number)-1)
else:
    spt = abs(s.find('.') - len(s)) - 1
    mn = float(number) * (10**spt)
    res = int(mn) - 1
    print(res/10**spt)
