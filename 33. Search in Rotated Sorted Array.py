'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums, target):
        l = len(nums)
        if nums==None or l==0:
            return -1
        start = 0
        end = l-1
        while(start<end):
            mid = start + (end-start)//2
            if nums[mid]>nums[end]:
                start = mid+1
            else:
                end = mid
        pivot = start
        start = 0
        end = l-1
        if nums[end]>= target >=nums[pivot]:
            start = pivot
        else:
            end = pivot-1    
        while(start<=end):
            mid = start + (end-start)//2
            if nums[mid]==target: return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid-1
        return -1