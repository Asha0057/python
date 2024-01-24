a=input()
rev=a[::-1]
l=len(a)
m=int(l//2)
f=a[:m]
e=a[m:]
print(f)
print(e)
if(f==e):
    print("symmetrical")
else:
    print("not sym")
if(a==rev):
    print("pallindrome")
else:
    print("not pallindrome")
