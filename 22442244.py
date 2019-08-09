nir=int(input())
magi=2**nir
zen=[]
for i in range(0,magi):
    l=bin(i)[2:].zenfill(nir)
    if(len(l)<len(bin(2**nir-1)[2:])):
        zen.append([l.count("1"),l])
    else:
        zen.append([l.count("1"),l])
zen.sort()
for i in range(len(zen)):
    print(zen[i][1])
