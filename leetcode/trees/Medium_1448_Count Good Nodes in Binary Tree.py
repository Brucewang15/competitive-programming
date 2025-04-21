# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getGood(node, upper):
            ans = 0
            if node is None:
                return 0
            if node.val >= upper:
                ans += 1
            
            ans += getGood(node.left, max(node.val, upper))
            ans += getGood(node.right, max(node.val, upper))
            return ans
        return getGood(root, root.val)