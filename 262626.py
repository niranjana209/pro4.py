bat = int(input())
lax = list(map(int, input().split()))
maximum = 0
ccccc = 0
any = lax[0]
for i in range(0,bat-1):
    if any < lax[i+1]:
        ccccc +=1
        any = lax[i+1]
    else:
        if max(lax[i+1:]) < any:
            any = lax[i+1]
print(ccccc+1)
