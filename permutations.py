from itertools import permutations 
k=list(input()) 
q = permutations(k) 
c=[]  
for i in list(q):
  s='' 
  for j in i:
    s+=j
  if s not in c:
    c.append(s)
    print(s)
