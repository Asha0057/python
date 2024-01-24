n=int(input("how many:"))
a=[]
for i in range(n):
    m=int(input())
    a.append(m)
#res=set(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)