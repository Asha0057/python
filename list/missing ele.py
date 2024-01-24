a=[]
n=int(input("how many?"))
for i in range(n-1):
     a.append(int(input()))
a.sort()
res=0
for i in range(1,len(a)):
    if(a[i]!=a[i-1]+1):
        res=a[i]-1
        print(res)