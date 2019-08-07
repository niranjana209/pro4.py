bi,kng=map(int,input().split())
mosd=list(map(int,input().split()))
mosd.sort()
mosd.reverse()
ssss=kng
pend=0
for i in mosd:
    if(s>=i):
        any=int(ssss/i)
        pend=pend+any
        ssss=ssss-any*i
    if ssss==0:
        break
if(s==0):
   print(pend)
else:
   print("it's not posiible to select coins in such a way that they sum upto",kng)
