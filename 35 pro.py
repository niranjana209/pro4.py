rat=input()
l1=list(set(rat))
xeen=1
anto=0
check=False
while True:
    ch=l1[anto]
    for y in range(0,len(rat)-xeen):
        if ch in rat[y:y+xeen]:
            check=True
        else:
            check=False
            anto=anto+1
            if anto>=len(l1):
             anto=0
             xeen=xeen+1
            break

    if check==True:
        break
print(xeen)
