'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for i in range(n)]
        count = 1
        up, down, left, right = 0, n, 0, n
        while(right>left and down>up):
            for i in range(left,right):
                res[up][i] = count
                count += 1
            up+=1

            for i in range(up,down):
                res[i][right-1] = count
                count+=1
            right-=1

            if(right>left):
                for i in range(right-1,left-1,-1):
                    res[down-1][i]=count
                    count+=1
                down-=1

            if(down>up):
                for i in range(down-1,up-1,-1):
                    res[i][left]=count
                    count+=1
                left+=1
                
        return res