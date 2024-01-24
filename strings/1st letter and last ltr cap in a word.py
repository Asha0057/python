n=input()
a=''
for i in range(len(n)-1):
    if(n[i-1]==" " or n[i+1]==" " or i==0 or i==n[-1]):
        a+=n[i].upper()
    else:
        a+=n[i]
a+=n[-1].upper()
print(a)