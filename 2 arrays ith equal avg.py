n=int(input())
l=input().split()
k=[]
r=[]
for x in l:
    k.append(int(x))
for x in range(0,len(k)):
    r1=0
    r2=0
    c1=0
    c2=0
    for y in range(x+1,len(k)):
        r1=r1+k[y]
        c1=c1+1
    if(c1>0):
        r1=int(r1/(c1))
    for z in range(0,x+1):
        r2=r2+k[z] 
        c2=c2+1
    if(c2>0):
        r2=int(r2/(c2))
    if(r1==r2):
        print("yes")
        break
else:
    print("no")
