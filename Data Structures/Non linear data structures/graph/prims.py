cost=[]
n=int(input('v:')) #vertex
m=int(input('e:'))#edges
for i in range(n):
    cost.append([0 for x in range(n)])
for i in range(m):
    c,d=map(int,input('c and d:').split()) #c-source d-dest
    cost[c][d]=int(input('cost'))
    cost[d][c]=int(input('cost'))
for i in range(n):
    for j in range(n):
        if cost[i][j]==0:
            cost[i][j]=999
    print()
vis=[0]*n
vis[1]=1
start=1
mincost=0
while start<n:
    minval=999
    for i in range(n):
        for j in range(n):
            if cost[i][j]<=minval:
                if vis[i]!=0:
                    minval=cost[i][j]
                    a=u=i
                    b=v=j
    if vis[u]==0 or vis[v]==0:
        print(f'edge {start}:({a} {b}) cost:{minval}')
        start+=1
        mincost+=minval
        vis[b]=1
    cost[a][b]=999
print('min cost=',mincost)