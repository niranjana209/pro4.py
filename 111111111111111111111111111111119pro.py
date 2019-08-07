bin=int(input())
boo=[]
mhs=[]
for i in range(bin):
    boo.append(list(map(int,input().split())))
for sing in boo:
    for num in sing:
        mhs.append(num)
mhs.sort()
for i in mhs:
    print(i,end=' ')
