a=[]
queue=[0]*20
front=0
rear=0
def enqueue(var):
    global rear
    queue[rear]=var
    rear=rear+1
def dequeue():
    global front
    front=front+1
def main():
    n=int(input('v:')) #vertex
    m=int(input('e:'))#edges
    for i in range(n):
        a.append([0 for x in range(n)])
    for i in range(m):
        c,d=map(int,input('c and d:').split()) #c-source d-dest
        a[c][d]=1
        a[d][c]=1
    """for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()"""
    vis = [0] * len(a)
    enqueue(1)
    vis[0]=1
    while front!=rear:
        curr=queue[front]
        print(curr,end=' ')
        dequeue()
        for i in range(len(a)):
            if a[curr-1][i]==1 and vis[i]==0:
                vis[i]=1
                enqueue(i+1)
if __name__=="__main__":
    main()
