bhuo,sis = map(int,input().split())
coost=0
lato = []
for i in range(bhuo):
      lato.append(input())
for i in range(bhuo):
      for j in range(sis-1):
            if lato[i][j] != 'R' and lato[i][j+1] != 'R' :
                  coost+=3
            elif lato[i][j] != 'G' and lato[i][j+1] != 'G':
                  coost+=5
print(coost)
