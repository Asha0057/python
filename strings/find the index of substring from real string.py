h=input()
n=input()
m = len(n)
c = 0
i=0
sp=-1
while(i<len(h) and i < len(n)):
    if h[i] == n[i]:
        c = c + 1
        if(c==1):
            sp=i
        if(c==m):
            break
    else:
        c=0
        sp=-1
    i=i+1
if (c == m):
    print(sp)
else:
    print("-1")