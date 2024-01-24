a=[]
right=[]
left=[]
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
mid=int(n/2)
print(mid)
for i in range(mid):
     right.append(a[i])
for i in range(mid,len(a)):
     left.append(a[i])

right.sort()
left.sort(reverse=True)
final=right+left
print(final)


