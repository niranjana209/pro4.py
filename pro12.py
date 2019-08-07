niran,arn=map(int,input().split())
fast=list(map(int,input().split()))
lin=[]
for i in range(0,arn):
     j,r=map(int,input().split())
     lin.append([j,r])
for i in range(arn):
     ower=lin[i][0]
     pper=lin[i][1]
     jim=sum(fast[ower-1:pper])
     print(jim)
