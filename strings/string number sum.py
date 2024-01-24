n=input()
a=[]
tot=0

for i in range(len(n)-1):
    if((n[i]>='1'and n[i]<='9')and (n[i+1]>='1'and n[i+1]<='9')):
        a.append(int(n[i]+n[i+1]))
    elif(n[i] >= '1' and n[i] <= '9'):
        a.append(int(n[i]))
print(a)
for i in range(len(a)):
    tot+=a[i]
print(tot)