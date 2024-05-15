n=int(input('size of table:'))
table = [[] for _ in range(n)]
print(table)
keys=[1,2,3,11,4,15,5,8,18]
m=10
for i in range(len(keys)):
    hash=(2*keys[i]+3)%m
    table[hash].append(keys[i])
for i in range(len(table)):
    print(table[i])

