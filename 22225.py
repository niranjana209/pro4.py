sel = int(input())
mag = list(map(int, input().split()))
maximum = 0
hk = 0
any = mag[0]
for i in range(0,sel-1):
    if any < mag[i+1]:
        hk +=1
        any = mag[i+1]
    else:
        if max(mag[i+1:]) < any:
            any = mag[i+1]
print(hk+1)
