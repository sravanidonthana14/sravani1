try:
	r=0
	n=str(input())
	c=[]
	k=str()
	for i in range (0,len(n)):
		c.append(n[i])
	if len(n)%2==0:
		j=len(n)
	else:
		j=len(n)-1
	while(r!=j):
		t=c[r]
		c[r]=c[r+1]
		c[r+1]=t
		r=r+2
	for i in range (0,len(c)):
		k=k+c[i]
	print (k)
except:
	print ("Invalid")
