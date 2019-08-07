man,pan = input().split()
pan = int(pan)
fake = False
nazi = list(map(int,input().split()))
for i in range(len(nazi)):
    for j in range(len(nazi)):
        if nazi[i]+nazi[j] == pan:
            fake = True
print("yes" if fake else "no") 
