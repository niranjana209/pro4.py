arn=int(input())
niran=1
while(niran<=arn and niran*2<=arn):
    niran=niran*2
if(niran==arn):
    print("0")
else:    
    print(arn-niran)
