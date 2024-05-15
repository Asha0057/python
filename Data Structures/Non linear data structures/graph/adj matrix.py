a=[]
n=int(input('v:')) #vertex
m=int(input('e:'))#edges
for i in range(n):
    a.append([0 for x in range(n)])
for i in range(m):
    c,d=map(int,input('c and d:').split()) #c-source d-dest
    a[c][d]=1 # for cost: int(input('cost'))
    a[d][c]=1 # for cost: int(input('cost'))
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()