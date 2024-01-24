n=input()
al=False
num=False

for i in range(len(n)):
    if n[i]>='a' and n[i]<='z' or n[i]>='A' and n[i]<='Z':
        al=True
    if(n[i]>='0' and n[i]<='9'):
        num=True
if(num and al):
    print("true")
else:
    print("false")
