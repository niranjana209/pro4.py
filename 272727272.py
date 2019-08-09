hav,ss=map(int,input().split())
zin=list(map(int,input().split()))
tsp=list(map(int,input().split()))
taan=[]
ciin=0
for i in range(hav):
    x=tsp[i]/zin[i]
    tan.append(x)
while ss>=0 and len(tan)>0:
    mindex=tan.index(max(tan))
    if ss>=zin[mindex]:
        ciin=ciin+tsp[mindex]
        ss=ss-zin[mindex]
    zin.pop(mindex)
    tsp.pop(mindex)
    taan.pop(mindex)
print(ciin)
