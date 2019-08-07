deer=int(input())
pine=list(map(int,input().split()))
ss=[1]*deer
for i in range(deer):
    if i==0:
        if pine[i]>pine[i+1]:
            ddd[i]=ddd[i]+ddd[i+1]
    elif i>0:
        if pine[i]>pine[i-1]:
           ddd[i]=ddd[i]+ddd[i-1]
print(sum(ddd))
