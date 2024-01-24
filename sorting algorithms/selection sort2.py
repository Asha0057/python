#selction sort without using min function
lists=[2,1,4,8,7,3,0]
for i in range(len(lists)-1):
    minz=lists[i]
    for j in range(i+1,len(lists)):
        if(minz>lists[j]):
            minz = lists[j]
            index_val = lists.index(minz, i)
            lists[i], lists[index_val] = lists[index_val], lists[i]

print(lists)
