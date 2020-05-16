'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        queensColumn = [-1]*n
        placeQueens(0, queensColumn, n, result)
        return len(result)


def isValidPos(queensColumn, col, row):
    valid = True
    for i in range(row):

        if queensColumn[i]==col:
            valid = False

        if abs(col-queensColumn[i])==abs(row-i):
            valid = False

    return valid


def placeQueens(row, queensColumn, n, result):
    if row==n:
        result.append(1)
        return
    
    for i in range(n):
        if isValidPos(queensColumn, i, row):
            queensColumn[row] = i
            placeQueens(row+1, queensColumn, n, result)