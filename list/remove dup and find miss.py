nums=list(map(int,input().split()))
nums.sort()
a=[]
i=0
while(i<len(nums)-1):
    if(nums[i]==nums[i+1]):
        a.append(nums[i])
        print(a)
    i=i+1
for j in range(1,len(nums)+1):
    if j not in nums:
        a.append(j)

print(a)