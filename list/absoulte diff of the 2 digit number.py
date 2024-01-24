n=int(input())
for i in range(10,n):
        temp=i
        rem=i%10
        l=i//10
        if abs(l-rem)==1:
            print(temp)
if(n<10):
    print("-1")