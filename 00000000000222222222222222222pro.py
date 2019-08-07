sun=int(input())
bhvi=list(map(int,input().split()))[:sun]
zia=sum(bhvi[0:sun:2])
ako=sum(bhvi[1:sun:2])
if zia>ako:
  print(zia)
else:
  print(ako)
