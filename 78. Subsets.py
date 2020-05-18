'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums):
        answer = []
        helper(nums, 0, [], answer)
        return answer
        
        
def helper(nums, index, cur, answer):
    # print(cur)
    answer.append(cur)
    for i in range(index, len(nums)):
        helper(nums, i+1, cur+[nums[i]], answer)