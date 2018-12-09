p=int(input(""))
s=0
for x in range(1,p+1):
   if(p%x==0):
    s=s+1
if(s==2):
    print("yes")
else:
    print("no")
