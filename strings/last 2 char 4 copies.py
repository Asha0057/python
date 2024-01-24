n=input()
b=''
if(len(n)>2):
    b+=n[-2]
    b+=n[-1]
    for i in range(4):
        print(b,end='')
else:
    print(n)