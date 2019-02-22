k=input("")
q=input("")
start=0
while start<min(len(k),len(q)):
    if k[start]!=q[start]:
        break
    start+=1
print(k[:start])
