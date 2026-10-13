# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        if root.right and root.left:
            root.right, root.left = root.left, root.right

            self.invertTree(root.right) 
            self.invertTree(root.left)

        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        else:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        
        return root

        




        