s,r=map(str,input().split())
e=0
for x in range(0,len(s)):
    if((ord(s[x])-ord(s[x-1]))!=(ord(r[x])-ord(r[x-1]))):
         e=e+1
if(e>0):
      print ("no")
else:
     print ("yes")
