'''
Given an array nums of n integers and an integer target, are there elements a, b, c, 
and d in nums such that a + b + c + d = target? Find all unique quadruplets in the 
array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums, target):
        l=len(nums)
        res = []
        nums.sort()
        for i in range(l-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,l-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                f = j+1
                b = l-1
                while(f<b):
                    summ = nums[i]+nums[j]+nums[f]+nums[b]
                    if summ>target:
                        b -= 1
                    elif summ<target:
                        f += 1
                    else:
                        res.append([nums[i],nums[j],nums[f],nums[b]])
                        while f<b and nums[f]==nums[f+1]:
                            f += 1
                        while f<b and nums[b]==nums[b-1]:
                            b -= 1
                        f += 1
                        b -+ 1
        return res