bhbh,ziiz=map(int,input().split())
skiit=[]
for i in range(0,bhbh):
    aaa=[int(sv) for sv in input().split()]
    skiit.append(sorted(aaa))
for i in range(0,len(skiit[0])):
  #print(skiit[i])
  for j in range(0,len(skiit)-1):
    if skiit[j][i]>skiit[j+1][i]:
      skiit[j][i],skiit[j+1][i]=skiit[j+1][i],skiit[j][i]
for i in skiit:
  print(*i)
