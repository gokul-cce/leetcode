# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.left == None and root.right == None:
            if root.val == targetSum:
                return True
        targetSum -= root.val
        left = self.hasPathSum(root.left,targetSum)
        right = self.hasPathSum(root.right,targetSum)
        return left or right


        