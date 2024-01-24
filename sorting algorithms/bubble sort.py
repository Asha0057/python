#bubble sort:  compares two adjacent elements and swaps them

l1=[]
n=int(input("how many?"))
for i in range(n):
    l1.append(int(input()))
for j in range(len(l1)-1):
    for i in range(len(l1)-1):
        if(l1[i]>l1[i+1]):
            l1[i],l1[i+1]=l1[i+1],l1[i]
            print(l1)
print("sorterd:",l1)