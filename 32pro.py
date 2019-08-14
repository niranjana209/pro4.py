bhoo,zez=map(int,input().split())
skit=[]
for i in range(0,bhoo):
    ara=[int(sv) for sv in input().split()]
    sky.append(sorted(ara))
for i in range(0,len(sky[0])):
  #print(sky[i])
  for j in range(0,len(sky)-1):
    if sky[j][i]>sky[j+1][i]:
      sky[j][i],sky[j+1][i]=sky[j+1][i],sky[j][i]
for i in sky:
  print(*i)
