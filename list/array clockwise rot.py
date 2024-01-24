'''a=[]
n=int(input("how many?"))
for i in range(n):
    a.append(int(input()))
rot=int(input("rot:"))

for i in range(rot):
    temp = a[-1]
    for j in range(len(a)-1,0,-1):
        a[j]=a[j-1]
    a[0]=temp
print(a)
'''
#or:
'''
a=[]
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
rot=int(input("rot:"))
res=[a[i] for i in range(-rot,len(a)-rot)]
print(res)
'''
#or

a=[]
n=int(input("enter no of rotations:"))
size=int(input("enter how many elements:"))
def rotation(n,a):
    n=n%len(a)
    print(a[-n:]+a[:-n])
for i in range(size):
     a.append(int(input()))
     rotation(n,a)



