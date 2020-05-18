'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        recursion(nums, 0, [], result)
        return result
               
def recursion(nums, index, path, result):
    result.append(path)
    for i in range(index, len(nums)):
        if i>index and nums[i]==nums[i-1]:
            continue
        recursion(nums, i+1, path+[nums[i]], result)