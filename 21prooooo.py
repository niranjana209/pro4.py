niran=int(input())
magi=list(map(int,input().split()))
ans=int(niran/2)
ranji=magi[:ans]
magi=magi[ans::]
if ((sum(ranji)//len(ranji))==(sum(man)//len(man))):
    print("yes")
else:
    print("no")
