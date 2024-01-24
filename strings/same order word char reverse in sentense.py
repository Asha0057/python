s=input()
st=''
i = 0
sp = -1
while i < len(s):
    if(s[i]==' '):
        for j in range(i-1,sp,-1):
            st+=s[j]
        st+=' '
        sp=i
    i=i+1
for j in range(len(s) - 1, sp, -1):
    st += s[j]
print(st)