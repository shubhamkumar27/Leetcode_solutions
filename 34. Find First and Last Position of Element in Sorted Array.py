'''
Given an array of integers nums sorted in ascending order, find the starting and ending 
position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums, target):
        if len(nums)==0:
            return [-1, -1]
        result = [-1, -1]
        l = len(nums)
        i = 0
        j = l-1
        while(i<j):
            mid = i + (j-i)//2
            if nums[mid]<target:
                i = mid+1
            else:
                j = mid
        if nums[i] != target:
            return result
        result[0]=i
        j = l-1
        while(i<j):
            print(i,j)
            mid = i + (j-i)//2 + 1
            if nums[mid]>target:
                j = mid-1
            else:
                i = mid
        result[1]=i
        return result