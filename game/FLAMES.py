ff=input("enter name:(girl)")
mm=input("enter name:(boy)")
f=list(ff)
m=list(mm)
f.sort()
if(f>m):
    print(f)
if(m<f):
    for i in range(len(f)):
        if(len(m)>=len(f)):
            break
        m.append(0)
for i in range(len(f)):
    for j in range(len(m)):
        if(f[i]==m[j]):
            f[i]=0
            m[j]=0
c=0
print(m)
print(f)
tot=m+f
for i in range(len(tot)):
    if(tot[i]!=0):
        c=c+1
flames=['F','L','A','M','E','S']
i = 0
while len(flames) > 1:
    i = (c + i - 1) % len(flames)
    flames.pop(i)
print("The result is: ", flames[0])

"""c1 = 0
zc = 0
combination = 6 * c
frame = []
flames_copy = flames[:]

i = 0
while(i < c * c):
    c1 = c1 + 1
    print(c1)
    if(c1 == c):
        flames_copy[c1] = 0
        zc = zc + 1
        c1 = 0
        if(zc == len(flames_copy)):
            break
    if(c1 == len(flames_copy)):
        c1 = 0
    i = i + 1
print(flames_copy)"""

