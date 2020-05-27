'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root==None:
            return result
        
        fromLeft = True
        queue = [root]
        
        while(len(queue)):
            levelNodes = len(queue)
            currentLevel = [None]*levelNodes
            
            for i in range(1, levelNodes+1):
                node = queue.pop(0)
                
                if fromLeft:
                    currentLevel[i-1] = node.val
                else:
                    currentLevel[-i] = node.val
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)  
            result.append(currentLevel)
            fromLeft = not fromLeft

        return result