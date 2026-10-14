# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        #Calculate height
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            #Keep track of longest diameter
            self.dia = max(self.dia, left + right)
            
            #return height
            return 1 + max(left, right)
        
        dfs(root)

        return self.dia
        