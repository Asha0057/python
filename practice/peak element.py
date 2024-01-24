a=[]
n=int(input("how many?"))
for i in range(n):
    a.append(int(input()))
i = 0
j=i+1
k=j+1
for i in range(len(a)-2):

    if(a[j]>a[i] and a[j]>a[k]):
        print("peak:",a[j])
