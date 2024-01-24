n=input()
s1=input()
s2=input()
m=n.split()
a=m.index(s1)
b=m.index(s2)
for i in range(a+1,b):
    print(m[i],end=" ")
"""
print(''.join(n.split(s1)[1].split(s2)[0]).strip())
"""