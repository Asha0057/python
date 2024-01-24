s=input()
k=int(input())
ss=list(s)
#print(ss)
for i in range(0,len(ss),2*k):
    ss[i],ss[i+1]=ss[i+1],ss[i]
st=''.join(ss)
print(st)
#or
#this works for all test cases:
ss=list(s)
for i in range(0,len(ss),2*k):
    ss[i:i + k] = reversed(ss[i:i + k])
st=''.join(ss)
print(st)