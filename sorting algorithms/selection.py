#find the min val from the whole list and swaps to the first index,
# then finds the next smallest element and swaps that to 2nd index, continues..

#ascending order
list1=[1,5,3,4,2,4]
for i in range(len(list1)-1):
    min_val = min(list1[i:]) #checks from 'i' eg:if i=2 then checks all from 2 except 0,1
    index = list1.index(min_val,i)
    list1[i],list1[index]=list1[index],list1[i]
print(list1)

#decending order
for i in range(len(list1)-1):
    max_val = max(list1[i:]) #checks from 'i' eg:if i=2 then checks all from 2 except 0,1
    index = list1.index(max_val,i)
    list1[i],list1[index]=list1[index],list1[i]
print(list1)
