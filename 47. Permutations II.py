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