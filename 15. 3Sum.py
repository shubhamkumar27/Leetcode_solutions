'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        l = len(nums)
        nums.sort()
        result = []
        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            f = i+1
            b = l-1
            while(f<b):
                summ = nums[i]+nums[f]+nums[b]
                if summ>0:
                    b -= 1
                elif summ<0:
                    f += 1
                else:
                    result.append([nums[i],nums[f],nums[b]])
                    while f<b and nums[f]==nums[f+1]:
                        f += 1
                    while f<b and nums[b]==nums[b-1]:
                        b -= 1
                    f += 1
                    b -= 1
        return result