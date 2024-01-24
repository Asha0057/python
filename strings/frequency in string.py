a=input()
check=input()
c=0
dict={}
for i in check:
    for j in a:
        if(i==j):
            c=c+1
    dict[i]=c
    c=0

print(dict)