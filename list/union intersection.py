a=[]
b=[]
c=[]
c1=0
n=int(input("how many?"))
m=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
for i in range(m):
     b.append(int(input()))
c.extend(a)
for i in range(len(b)):
     if b[i] not in c:
          c.append(b[i])
     else:
          c1=c1+1

print(len(c))
print(c1)