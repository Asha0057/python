s=input()
'''
m=s.split()
print(m)
for i in range(len(m)-1,-1,-1):
    print(m[i],end =" ")
    '''
#or
ss=''
sp=len(s)
for i in range(len(s)-1,0,-1):
    if(s[i]==' '):
        for j in range(i,sp):
            ss+=s[j]
        ss+=' '
        sp=i
for i in range(sp):
    ss+=s[i]
print(ss.strip())