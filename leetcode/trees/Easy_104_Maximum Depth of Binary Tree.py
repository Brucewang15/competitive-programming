# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # stack approach
        # if root is None:
        #     return 0
        # stack = deque([root])
        # level = 0
        # while stack:
        #     for i in range(len(stack)):
        #         node = stack.popleft()
        #         if node.left is not None:
        #             stack.append(node.left)
        #         if node.right is not None:
        #             stack.append(node.right)
        #     level += 1
        # return level
        def getHeight(node):
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        return getHeight(root)
        