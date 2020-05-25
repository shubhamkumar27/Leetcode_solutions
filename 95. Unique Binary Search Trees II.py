'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return None
        lis = [i for i in range(1,n+1)]
        return treeHelper(lis)
        
        
def treeHelper(lis):
    if len(lis)==0:
        return [None]
    
    val = []
    for i in range(len(lis)):
        left = treeHelper(lis[:i])
        if i<len(lis)-1:
            right = treeHelper(lis[i+1:])
        else:
            right = [None]
        for l in range(len(left)):
            for r in range(len(right)):
                root = TreeNode(lis[i])
                root.left = left[l]
                root.right = right[r]
                val.append(root)
    return val
    