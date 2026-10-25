# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []

        queue = deque()
        queue.append(root)

        while queue:
            temp_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp_res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if temp_res:
                res.append(temp_res)

        
        return res
        



        