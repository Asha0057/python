n=int(input("how many:"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
a.sort()
ex=(n*(n+1))//2
ss=sum(a)
result=ex - ss
print(result)
