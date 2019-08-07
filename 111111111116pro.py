kum=int(input())
pine=list(map(int,input().split()))
fun=[1]*kum
for i in range(kum):
    if i==0:
        if pine[i]>pine[i+1]:
            fun[i]=fun[i]+fun[i+1]
    elif i>0:
        if pine[i]>pine[i-1]:
            fun[i]=fun[i]+fun[i-1]
print(sum(fun))
