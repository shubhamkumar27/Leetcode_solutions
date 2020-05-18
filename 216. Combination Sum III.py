'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        recursion(1, 0, k, n, result, [])
        return result
        
        
def recursion(index, total, k, n, result, current):
    if len(current)==k:
        if total==n:
            result.append(current)
        return
    
    for i in range(index, 10):
        recursion(i+1, total+i, k, n, result, current+[i])
