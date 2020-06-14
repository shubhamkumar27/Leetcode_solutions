'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        
        for num in nums:
            temp = root
            
            for i in range(31, -1, -1):
                bit = (num>>i)&1
                
                if bit:
                    if temp.one==None:
                        temp.one = TrieNode()
                    temp = temp.one
                else:
                    if temp.zero==None:
                        temp.zero = TrieNode()
                    temp = temp.zero
        
        maxans = 0
        for num in nums:
            temp = root
            ans = 0
            for i in range(31,-1,-1):
                bit = (num>>i)&1
                
                if bit and temp.zero:
                    ans += (1<<i)
                    temp = temp.zero
                elif bit==0 and temp.one:
                    ans += (1<<i)
                    temp = temp.one
                else:
                    temp = temp.one or temp.zero
            
            maxans = max(maxans, ans)
            
        return maxans
                    
