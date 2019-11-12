'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide 
and conquer approach, which is more subtle.
'''

######### METHOD 1 #################
class Solution:
    def maxSubArray(self, nums):
        curmax = 0
        largest = -2**31
        for i in range(len(nums)):
            curmax += nums[i]
            if largest<curmax:
                largest = curmax
            if curmax<=0:
                curmax = 0
        return largest

######### METHOD 2 ##############
class Solution2:
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
            print(nums)
        return max(nums)