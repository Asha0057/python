
def binary(n,s,end,search):
    mid=(s+end)//2
    if(search==n[mid]):
        return mid
    elif(search>n[mid]):
        return binary(n,mid+1,end,search)
    elif(search<n[mid]):
        return binary(n,s,mid-1,search)

n=list(map(int,input().split()))
search=int(input())
s=0
n1=len(n)
end=n1-1
res=binary(n,s,end,search)
print(res)
