# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = []
    
    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)

        self.sol.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.postorder(root)
        return self.sol
        