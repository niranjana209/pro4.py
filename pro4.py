niran,vasu=map(str,input().split())
wavve=0
if len(niran)>len(vasu):
  niran,vasu=vasu,subu
i=0
while i<len(niran):
  wavve+=(ord(vasu[i])-ord(niran[i]))
  i+=1
for i in range(i,len(vasu)):
  wavve+=ord(vasu[i])-ord('a')+1
print(wavve)
