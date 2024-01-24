#method1
n=input()
m=n.split()
k=int(input())
a=[]
for i in range(len(m)):
    if(len(m[i])>k):
        print(m[i],end=' ')
#method2
for i in range(len(m)):
    if(m[i]!=' '):
        a.append(m[i])
for i in range(len(a)):
    if(len(a[i])>k):
        print(a[i],end=' ')