akk,nil=map(int,input().split())
list1=list(map(int,input().split()))
akk=[]
list1.insert(0,0)
for y in range(nil):
     sin=[]
     d=0
     vv,ff=map(int,input().split())
     for i in range(vv,ff+1):         
         d^=list1[i]     
     akk.append(d)
for y in akk:
     print(y)
