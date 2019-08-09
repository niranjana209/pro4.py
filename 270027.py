nir,sws=map(int,input().split())
zqz=list(map(int,input().split()))
vsbo=list(map(int,input().split()))
tane=[]
cinp=0
for i in range(nir):
    xr=vsbo[i]/zqz[i]
    tane.append(xr)
while sws>=0 and len(tane)>0:
    mindexs=tane.index(max(tane))
    if sws>=zqz[mindexs]:
        cinp=cinp+vsbo[mindexs
        sws=sws-zqz[mindexs]
    zqz.pop(mindexs)
    vsbo.pop(mindexs)
    tan.pop(mindexs)
print(cinp)
