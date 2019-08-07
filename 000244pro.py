fan=(input())
duk=0
for i in range(0,len(fan)):
    swr=(fan[:i]+fan[i+1:])
    if(int(swr) % 8==0):
        duk=1
        break
if(duk==1):
    print("yes")
else:
    print("no"
