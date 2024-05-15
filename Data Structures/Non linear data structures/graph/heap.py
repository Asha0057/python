def heap(a,n,i):
    large=i
    left=2*i+1
    right=2*i+2
    if left<n and a[large]>a[left]:
        large=left
    if right<n and a[large]>a[right]:
        large=right
    if large!=i:
        a[i],a[large]=a[large],a[i]
        heap(a,n,large)
def heapsort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        heap(a,n,i)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heap(a,i,0)
a=list(map(int,input().split()))
heapsort(a)
print(a)