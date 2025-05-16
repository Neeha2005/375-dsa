#Using Kadane Algorithm
def maxSubArray(nums):
    n = len(nums)
    max_sum = float('-inf')
    curr_sum = 0
    for start in range(n):
        curr_sum += nums[start]
        max_sum = max(max_sum,curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))