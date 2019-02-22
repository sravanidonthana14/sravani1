w,y=map(str,input().split(" "))
lw=len(w)
ly=len(y)
c=0
if ly>lw:
    n=ly-lw
    for i in range(n):
        w+=" "
elif lw>ly:
    e=""
    for i in range(ly):
        e+=w[i]
    w=e
    c=c+(lw-ly)
for i in range(len(w)):
    if w[i]!=y[i]:
        c+=1
print(c)
