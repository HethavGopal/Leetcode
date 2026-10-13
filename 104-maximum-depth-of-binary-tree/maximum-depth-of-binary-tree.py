# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        depth = 1

        if root.left and root.right:
            depth = max(self.maxDepth(root.right) + 1, self.maxDepth(root.left) + 1)
        elif root.left:
            depth = max(depth, self.maxDepth(root.left) + 1)
        else:
            depth = max(self.maxDepth(root.right) + 1, depth)

        return depth