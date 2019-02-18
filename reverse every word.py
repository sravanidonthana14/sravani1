z=input()
l=list(z.split())
q=[]
z=''
for i in range(len(l)):
	z+=l[i][::-1]+' '
print(z)
