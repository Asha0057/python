def act(s,f): #s-startTime f-finalTime
    a=len(f)
    i=0
    print(i,end=' ')
    for j in range(1,a):
        if s[j]>=f[i]:
            print(j,end=' ')
        i=j
s=list(map(int,input().split()))
f=list(map(int,input().split()))
f.sort()
act(s,f)

"""
#input:
5 8 3 1 9 11
2 4 8 9 16 17 #if unsorted sort the f first

#output: 
0 1 4 
"""