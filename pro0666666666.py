nirun1=int(input())
nirun2=list(map(int,input().split()))
aru=0
for e in range(len(nirun2)-2):
    for f in range(e+1,len(nirun2)-1):
        for g in range(f+1,len(nirun2)):
            if nirun2[e]<nirun2[f]<nirun2[g] and e<f<g:
                aru=aru+1
print(aru)
