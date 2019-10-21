'''
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        if l <= 1:
            return
        d = {}
        for i in range(l):
            try:
                return [d[nums[i]],i]
            except:
                d[target-nums[i]]=i