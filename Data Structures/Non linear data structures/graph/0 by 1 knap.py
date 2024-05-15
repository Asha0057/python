def knap(w,wt,val,n):
    k=[[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(w+1):
            if i==0 or w==0:
                k[i][w]=0
            elif wt[i]<=w:
                k[i][w]=max(val[i]+k[i-1][w-wt[i]],k[i-1][w])
            else:
                k[i][w]=k[i-1][w]
    return k[n][w]
weights=[0,3,4,6,5]
profits=[0,2,3,1,4]
w=8
n=4
print(knap(w,weights,profits,n))