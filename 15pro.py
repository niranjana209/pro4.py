sub=input()
kan=map(int,input().split())
sin=[]
for i in kan:
    kow=bin(i)
    sin.append(kow)
han=sorted(sin)
han.reverse()
for j in han:
    print(int(j,2))
