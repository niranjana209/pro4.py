ani=(input())
cute=0
for i in range(0,len(ani)):
    suro=(ani[:i]+ani[i+1:])
    if(int(suro) % 8==0):
        cute=1
        break
if(cute==1):
    print("yes")
else:
    print("no")
