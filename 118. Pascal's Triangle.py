'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i<2:
                ans.append([1]*(i+1))
            else:
                col = [1]*(i+1)
                l = 1
                r = i-1
                while(l<=r):
                    col[l] = ans[-1][l-1]+ans[-1][l]
                    col[r] = ans[-1][r-1]+ans[-1][r]
                    l+=1
                    r-=1
                ans.append(col)
                
        return ans
