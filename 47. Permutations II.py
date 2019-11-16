'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums):
        if len(nums)==0:
            return []
        result = []
        nums.sort()
        return self.recursive(nums,0,result)
    
        
    def recursive(self, nums, start, result):
        myset = set()
        if start>=len(nums)-1:
            #print(start,nums)
            result.append(nums[:])
            return result
        
        for i in range(start,len(nums)):
            #print(start,i)
            if nums[i] not in myset:
                myset.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                self.recursive(nums,start+1,result)
                nums[start], nums[i] = nums[i], nums[start]
            
        return result