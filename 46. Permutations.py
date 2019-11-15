'''
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        if len(nums)==0:
            return []
        result = []
        return self.recursive(nums, 0 ,result)
    
    def recursive(self,nums,start,result):
        if start>=len(nums)-1:
            result.append(nums[:])
            return result
            
        for i in range(start,len(nums)):
            nums[start],nums[i]=nums[i],nums[start]
            self.recursive(nums, start+1, result)
            nums[start],nums[i]=nums[i],nums[start]
        
        return result
