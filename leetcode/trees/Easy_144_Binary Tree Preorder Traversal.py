# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = []
    
    def preorder(self, node):
        if node:
            self.sol.append(node.val)

            self.preorder(node.left)
            self.preorder(node.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.sol
        