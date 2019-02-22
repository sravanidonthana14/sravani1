k=input("")
y=input("")
start = 0
while start < min(len(k), len(y)):
    if k[start] != y[start]:
        break
    start += 1
print(k[:start])
