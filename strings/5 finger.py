n=int(input())
m=n%8
if(m==1):
    print("thum")
elif(m==2 or m==0):
    print("index")
elif(m==3 or m==7):
    print("middle")
elif(m==5):
    print("last")
else:
    print("ring")
