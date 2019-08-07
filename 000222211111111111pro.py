bvi=int(input())
aah=list(map(int,input().split()))
anns=int(bvi/2)
ranj=aah[:anns]
manj=aah[anns::]
if ((sum(ranj)//len(ranj))==(sum(manj)//len(manj))):
    print("yes")
else:
    print("no")
