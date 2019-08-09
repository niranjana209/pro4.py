hav,sss=map(int,input().split())
zzzz=list(map(int,input().split()))
tpv=list(map(int,input().split()))
aan=[]
pin=0
for i in range(hav):
    x=tspv[i]/zzzz[i]
    aan.append(x)
while sss>=0 and len(aan)>0:
    mindex=aan.index(max(aan))
    if sss>=zzzz[mindex]:
        pin=pin+tspv[mindex]
        sss=sss-zzzz[mindex]
    zzzz.pop(mindex)
    tspv.pop(mindex)
    aan.pop(mindex)
print(pin)
