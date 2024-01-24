s1=list(map(str,input().split()))
s1.sort()
s1s=set(s1)
p=input()
ps=''.join(sorted(p))
c=0
m=[]
l=''
print(s1s)
if(len(s1s)!=len(ps)):
    print('false')
else:
    i=0
    j=0
    while(i<len(ps)-1):
        if(ps[i]==ps[i+1]):
            c=c+1
        else:
            m.append(s1s[j]*(c+1))
            l+=s1s[j]*(c+1)
            c=0
            j=j+1
        i = i + 1
    m.append(s1s[j] * (c + 1))
    if m == s1:
        print("true")
    else:
        print("false")
print(l)






