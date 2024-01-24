from collections import Counter
a=[]
n=int(input("how many?"))
for i in range(n):
     a.append(int(input()))
'''
dict={}
count=0
for i in range(len(a)):
     for j in range(len(a)):
          if a[i]==a[j]:
               count=count+1
     dict[a[i]]=count
     count = 0
print(dict)
'''
result=[item for items, c in Counter(a).most_common() for item in [items] * c]
print(result)