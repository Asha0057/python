n=input()
m=len(n)
c=0
for i in range(len(n)):
    if(n[i]=='0' or n[i]=='1'):
        c=c+1
print(c)
print(m)
if(c==m):
    print("yes")
else:
    print("no")

#or
n=input()
st=set(n)
p={'0','1'}
if(st==p or st=={'0'} or st=={'1'}):
    print("yes")
else:
    print("no")