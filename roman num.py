val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
S = str(input())
S = S.upper()
g = 0
while S:
    if len(S) == 1 or val[S[0]] >= val[S[1]]:
        g += val[S[0]]
        S = S[1:]
    else:
        g += val[S[1]] - val[S[0]]
        S = S[2:]
print (g)
