n=int(input('size of table:'))
table =[-1]*n
print(table)
c=0
keys=[3,2,9,6,11,13,7,12]
m=10
for i in range(len(keys)):
    hash=(2*keys[i]+3)%m
    if table[hash]==-1:
        table[hash]=(keys[i])
    else:
        for j in range(len(keys)):
            u=(hash+j)%m
            if table[u]==-1:
                table[u]=keys[i]
                break
for i in range(len(table)):
    print(table[i])