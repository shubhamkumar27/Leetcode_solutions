'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return helper(root.left, root.right)
        
        
def helper(left, right):
    if left==None or right==None:
        if left==right:
            return True
        else:
            return False
        
    if left.val!=right.val:
        return False
    
    l = helper(left.left, right.right)
    r = helper(left.right, right.left)
    
    return l and r
    