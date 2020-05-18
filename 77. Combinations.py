'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine(self, n: int, k: int):
        nums = [i for i in range(1, n+1)]
        result = []
        recursive(nums, k, 0, [], result)
        return result
        
        
def recursive(nums, k, index, path, result):
    if len(path)==k:
        result.append(path)
        return
        
    for i in range(index, len(nums)):
        recursive(nums, k, i+1, path+[nums[i]], result)