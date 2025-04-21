# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # O(N^2) approach
        ans = 0

        def getAns(node):
            nonlocal ans
            if node is None:
                return []
            
            lst = [node.val]
            left = getAns(node.left)
            right = getAns(node.right)
            if node.val == targetSum:
                ans += 1
            for i in left:
                if node.val + i == targetSum:
                    ans += 1
                lst.append(node.val + i)
            for i in right:
                if node.val + i == targetSum:
                    ans += 1
                lst.append(node.val + i)
            return lst
        getAns(root)
        return ans

        
