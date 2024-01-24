a=[]
count=0
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
     if(a[i]==0):
         count=count+1
m=int(input("pots:"))
if(count%m==1):
    print("true")
else:
    print("false")