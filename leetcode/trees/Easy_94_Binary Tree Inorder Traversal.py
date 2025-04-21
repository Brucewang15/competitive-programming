# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution with classes
    #
    # def __init__(self):
    #     self.solution = []

    # def inorder(self, node):
    #     if node is None:
    #         return
        
    #     self.inorder(node.left)
    #     self.solution.append(node.val)
    #     self.inorder(node.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            sol.append(node.val)
            inorder(node.right)
        inorder(root)
        return sol

        
                

        