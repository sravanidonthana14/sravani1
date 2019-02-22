u,v=input().split()
v=int(v)
x=len(u)
w=[]
for j in range(0,x):
	r=u[j]
	w.append(r)
d=x-v
a=[]
for j in range(v,x):
	r=w[j]
	a.append(r)
print("".join(a))
