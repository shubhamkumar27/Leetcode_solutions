'''
Given an array nums of n integers and an integer target, find three integers in 
nums such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        l = len(nums)
        nums.sort()
        min_diff = 2**31-1
        fsum = 0
        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            f = i+1
            b = l-1
            while(f<b):
                summ = nums[i]+nums[f]+nums[b]
                diff = abs(target-summ)
                if diff<min_diff:
                    min_diff = diff
                    fsum = summ
                if summ>target:
                    b -= 1
                elif summ<target:
                    f += 1
                else:
                    return summ
        return fsum