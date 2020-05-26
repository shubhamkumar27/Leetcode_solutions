'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#################### RECURSIVE ############################
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inOrder = []
        inOrderTraversal(root, inOrder)
        return inOrder
        
def inOrderTraversal(root, inOrder):
    if root==None:
        return
    inOrderTraversal(root.left, inOrder)
    inOrder.append(root.val)
    inOrderTraversal(root.right, inOrder)


################### ITERATIVE ###########################
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        inOrder = []
        while root or len(stack)!=0:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
                inOrder.append(node.val)
        return inOrder