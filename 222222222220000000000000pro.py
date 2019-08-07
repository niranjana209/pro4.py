niran,arn=map(int,input().split())
joo=list(map(int,input().split()))
joo.sort()
joo.reverse()
ssss=arn
pin=0
for i in joo:
    if(ssss>=i):
        any=int(ssss/i)
        peng=peng+any
        ssss=ssss-any*i
    if ssss==0:
        break
if(ssss==0):
   print(peng)
else:
   print("it's not posiible to select coins in such a way that they sum upto",arn)
