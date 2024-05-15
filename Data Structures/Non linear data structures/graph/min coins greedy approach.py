def find(n):
    a=[1,2,5,10,20,50,100,200,500,1000]
    s=len(a)
    i=s-1
    c=[]
    while(i>=0):
        while(n>=a[i]):
            c.append(a[i])
            n-=a[i]
        i-=1
    for i in range(len(c)):
        print(c[i],end=' ')
n=int(input())
find(n)
