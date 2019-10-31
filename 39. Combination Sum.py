'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates, target):
        if len(candidates)==0:
            return []
        res = []
        candidates.sort()
        self.recursive(candidates,target,0,res,[])
        return res
        
    def recursive(self, nums, target, index, res, path):
        if target==0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            # print(i,res,target)
            if nums[i]>target:
                break
            self.recursive(nums,target-nums[i],i,res,path+[nums[i]])