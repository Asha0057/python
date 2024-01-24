a=[]
b=[]
pro=1
action=['C','D','+','-']
n=int(input("how many?"))
for i in range(n):
     a.append(input())
for i in range(len(a)):
    if(a[i] not in action):
        b.append(a[i])
    if(a[i]=='D'):
        for i in range(len(b)):
            pro*=int(a[i])
        b.append(pro)
    elif(a[i=='+']):

        b.append(sumz)
print(b)