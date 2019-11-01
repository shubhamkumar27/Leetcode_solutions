'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates, target):
        if len(candidates)==0:
            return []
        candidates.sort()
        print(candidates)
        result = []
        self.recursive(candidates,target,0,[],result)
        return result
    
    def recursive(self, nums, target, index, path, result):
        if target == 0:
            result.append(path)
            return
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            if nums[i]>target:
                return
            self.recursive(nums,target-nums[i],i+1,path+[nums[i]],result)