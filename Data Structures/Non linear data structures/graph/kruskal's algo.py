def find(p,i):
    if p[i]==i:
        return i
    return find(p,p[i])
def union(p,rank,x,y):
    xroot=find(p,x)
    yroot=find(p,y)
    if rank[xroot]<rank[yroot]:
        p[xroot]=yroot
    elif rank[xroot]>rank[yroot]:
        p[yroot]=xroot
    else:
        p[yroot]=xroot
        rank[xroot]+=1
n=int(input('enter node:'))
print('enter matrix')
cost=[]
for i in range(n):
    row=list(map(int,input().split()))
    cost.append(row)
edges=[]
for i in range(n):
    for j in range(i+1,n):
        if cost[i][j]!=0:
            edges.append((i,j,cost[i][j]))
print(edges)
edges.sort(key=lambda x:x[2])
p=[i for i in range(n)]
mst_edges=[]
rank=[]*n
mincost=0
print(p)
for edge in edges:
    u, v, weight=edge
    x=find(p,u)
    y=find(p,v)
    if x!=y:
        mst_edges.append((u,v))
        mincost+=weight
        union(p,rank,x,y)
print("min:")
for i in mst_edges:
    print("edge:",i)
print("min cost:",mincost)
