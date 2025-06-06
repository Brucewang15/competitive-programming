# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def check(node, val):
            if node is None:
                return None
            if node.val == val:
                return node
            if node.val < val:
                return check(node.right, val)
            return check(node.left, val)
        return check(root, val)
            
        