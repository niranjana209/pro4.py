an=(input())
hat=0
for i in range(0,len(an)):
    srr=(an[:i]+an[i+1:])
    if(int(srr) % 8==0):
        hat=1
        break
if(hat==1):
    print("yes")
else:
    print("no")
