n = int(input())
tem = []
press = []
for _ in range(n):
    t,p = [float(i) for i in input().split()]
    tem.append(t)
    if -70 < t < 80:
        press.append(p)

s_tem = sum(tem)/len(tem)
s_press = sum(press)/len(press)
print(f'{s_tem:.4f} {s_press:.4f}')
