can=int(input())
okk=list(map(int,input().split()))
okk.sort()
sind=0
svps=0
for i in range(len(okk)):
    if okk[i]>=sind:
        svps=svps+1
    sind=sind+okk[i]
print(svps)
