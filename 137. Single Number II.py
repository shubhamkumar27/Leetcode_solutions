'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count=0
            for num in nums:
                if (num>>i)&1:
                    count+=1
            ans |= (count%3)<<i
        if ans>2**31 -1:
            return ans-2**32
        return ans