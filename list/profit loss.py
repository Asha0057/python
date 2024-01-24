a=[]
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
max=0
for i in range(1,len(a)):
    if(a[i]>a[i-1]):
        max+=a[i]-a[i-1]
    print(max)
print(max)
