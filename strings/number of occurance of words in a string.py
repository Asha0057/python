s1=input("string:")
li=s1.split()
d={}
for i in li:
    if(i not in d.keys()):
        d[i]=0
    d[i]=d[i]+1
print(d)