a=[]
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
peak=max(a)
print(peak)
#print(peak)
#right
for i in range(peak+1,len(a)):
    for j in range(peak+2,len(a)):
        if(a[j]>=a[i]):
            print("not a mountain array")
            break
        else:
            continue
        break
    else:
        print("mountain array")
#left
for i in range(peak-1,0,-1):
    for j in range(peak-2,0,-1):
        if(a[i]>=a[j]):
            print("not a mountain array")
            break
        else:
            continue
        break
    else:
        print("mountain array")