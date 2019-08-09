bil=int(input())
magi=2**bil
z=[]
for i in range(0,magi):
    l=bin(i)[2:].zfill(bil)
    if(len(l)<len(bin(2**bil-1)[2:])):
        z.append([l.count("1"),l])
    else:
        z.append([l.count("1"),l])
z.sort()
for i in range(len(z)):
    print(z[i][1])
