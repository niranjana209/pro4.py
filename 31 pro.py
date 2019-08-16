bhoo=input()
fllagg=0
for i in range(0,len(bhoo)-1):
  for j in range(i+1,len(bhoo)):
    if bhoo[i]<bhoo[j]:
      fllagg=1
      print(bhoo[j:])
      break
  if fllagg==1:
    break
else:
  print(bhoo)
