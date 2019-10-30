'''
Implement next permutation, which rearranges numbers into the lexicographically next greater 
permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order 
(ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs 
are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums==[] or nums == None or len(nums)==1:
            return
        l = len(nums)
        i = l-1
        while(nums[i-1]>=nums[i] and i>0):
            i -= 1
        start = i
        last = l-1
        while(start<last):
            nums[start],nums[last]=nums[last],nums[start]
            start += 1
            last -= 1
        if i==0:
            return
        else:
            j = i-1
            while i<l:
                if nums[i]>nums[j]:
                    nums[j],nums[i]=nums[i],nums[j]
                    break
                i += 1        
            return