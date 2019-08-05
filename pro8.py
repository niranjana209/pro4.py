import math
nir,vas=map(int,input().split())
siva=[]
denu=list(map(int,input().split()))
for i in range(0,vas):
    lacks,hac=map(int,input().split())
    siva.append([lacks,hac])
for i in siva:
    duck=i[0]-1
    hat=i[1]-1
    print(math.gcd(denu[duck],denu[hat]))
