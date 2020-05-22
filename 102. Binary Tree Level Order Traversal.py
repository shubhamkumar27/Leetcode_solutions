'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        recursive(root, 0, result)
        return result
    
def recursive(root, level, result):
    if root==None:
        return
    
    if len(result)<level+1:
        result.append([])
        
    result[level].append(root.val)
    recursive(root.left, level+1, result)
    recursive(root.right, level+1, result)
    