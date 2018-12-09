m=int(input(""))
p=list(map(int,str(m)))
q=list(map(lambda x:x**3,p))
if(sum(q)==m):
    print("yes")
else:
    print("no")
