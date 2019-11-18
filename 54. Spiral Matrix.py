'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==0:
            return []
        if len(matrix)==1:
            return matrix[0]
        up, down, left, right = 0, len(matrix), 0, len(matrix[0])
        res = []
        while(up<=down-1 and left<=right-1):
            for i in range(left,right):
                res.append(matrix[up][i])
            up+=1

            for i in range(up,down):
                res.append(matrix[i][right-1])
            right-=1
            
            if(down>up):
                for i in range(right-1,left-1,-1):
                    res.append(matrix[down-1][i])
                down-=1
            
            if(right>left):
                for i in range(down-1,up-1,-1):
                    res.append(matrix[i][left])
                left+=1

        return res