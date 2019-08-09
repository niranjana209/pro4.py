hav,ss=map(int,input().split())
zzzz=list(map(int,input().split()))
tpv=list(map(int,input().split()))
tan=[]
cin=0
for i in range(hav):
    x=tspv[i]/zzzz[i]
    tan.append(x)
while ss>=0 and len(tan)>0:
    mindex=tan.index(max(tan))
    if ss>=zzzz[mindex]:
        cin=cin+tspv[mindex]
        ss=ss-zzzz[mindex]
    zzzz.pop(mindex)
    tspv.pop(mindex)
    tan.pop(mindex)
print(cin)
