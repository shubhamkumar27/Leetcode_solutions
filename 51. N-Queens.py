'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens 
attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queensColumn = [-1]*n
        placeQueens(0, queensColumn,n, result)
        return result

def isValidPos(queensColumn, col, row):
    valid = True
    for i in range(row):

        if queensColumn[i]==col:
            valid = False

        if abs(col-queensColumn[i])==abs(row-i):
            valid = False

    return valid

def addResult(queensColumn,n, result):
    res = []
    for i in range(n):
        cur = ''
        for j in range(n):
            if j==queensColumn[i]:
                cur+='Q'
            else:
                cur+='.'
        res.append(cur)
    result.append(res)


def placeQueens(row, queensColumn, n, result):
    if row==n:
        addResult(queensColumn, n, result)
        return
    
    for i in range(n):
        if isValidPos(queensColumn, i, row):
            queensColumn[row] = i
            placeQueens(row+1, queensColumn, n, result)