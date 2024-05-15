def maxSubArray(nums):
    maxx = nums[0] #to store maximum value frst initialise to 1st number
    sums = 0 #to calculate curr sum
    for i in nums:
        if sums < 0: #sum is -ve then set to 0
            sums = 0
        sums += i
        maxx = max(maxx, sums) #find the max btw sum and maxx
    return maxx
nums = [-2,1,-3,4,-1,2,1,-5,4]
s=maxSubArray(nums)
print(s)
"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""