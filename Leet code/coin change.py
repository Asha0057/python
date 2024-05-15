def coin(a,n,val):
    if val==0:
        return 1
    if val<0:
        return 0
    if n<=0:
        return 0
    return coin(a,n-1,val)+coin(a,n,val-a[n-1])
s=int(input('target:'))
a=list(map(int,input('list:').split()))
n=len(a)
print(coin(a,n,s))