netu=input()
llack=list(map(int,input().split()))
casf=0
for i in range(0,len(llack)-2):
    for j in range(i+1,len(llack)-1):
        for k in range(j+1,len(llack)):
            if llack[i]>llack[j] and llack[j]>llack[k]:
                casf+=1
print(casf)
