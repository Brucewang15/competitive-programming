# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaves(node, ans):
            if node is None:
                return
            if node.left is None and node.right is None:
                ans.append(node.val)
                return
            getLeaves(node.left, ans)
            getLeaves(node.right, ans)
        
        leaves1 = []
        leaves2 = []

        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)
        return leaves1 == leaves2