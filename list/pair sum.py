a=[]
b=[]
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
k=int(input())
count=0

for i in range(len(a)):
    for j in range(1,len(a)):
        if(a[i]+a[j]==k):
            if(i and j not in b):
                b.insert(a[i],a[j])
                count=count+1
print(count)
