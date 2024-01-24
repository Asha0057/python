m=[]
for i in range(5):
    m.append((int(input())))
#sorting
for j in range(len(m)-1):
    for i in range(len(m)-1):
        if(m[i]>m[i+1]):
            m[i],m[i+1]=m[i+1],m[i]
print(m)#sorted

#print mx and min
end=-1
f=0
for i in range(len(m)):
    if (m[end] == m[f]):
        break
    else:
        print(m[end],m[f],end=' ')
        end=end-1
        f=f+1
print(m[f])