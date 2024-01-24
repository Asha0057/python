s=input()
goal=input()
l=list(s)
i=0
while(i<len(l)):
    temp = l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
    l[-1]=temp
    final=''.join(l)
    if(final==goal):
        print("true")
        break
    i=i+1
if(final!=goal):
    print("false")
