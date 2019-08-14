ccc=int(input())
zen=0
xon=0
bhoo=[]
while zen<90 and zen<ccc:
  son=0
  for j in str(ccc-zen):
    son+=int(j)
  if son+(ccc-zen)==ccc:
    xon+=1
    bhoo.append(ccc-zen)
  zen+=1
print(xon)
for zen in bhoo:
  print(zen)
